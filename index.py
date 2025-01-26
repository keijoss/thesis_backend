from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Initialize Flask app  
app = Flask(__name__)

# Load the trained model and dataset
model_path = "dataset/3quiz1model.pkl"
data_path = "dataset/questions.csv"

# Load model and feature names
with open(model_path, "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
model_features = model_data["features"]  # Load feature names

data = pd.read_csv(data_path)

@app.route('/predict/', methods=['POST'])
def predict():
    try:
        # Get JSON input from request
        input_data = request.json

        # Extract answers and question IDs
        student_answers = input_data.get("answers", [])
        if not student_answers:
            return jsonify({"error": "No answers provided"}), 400

        # Merge student answers with the dataset
        answers_df = pd.DataFrame(student_answers)
        data_with_answers = data.merge(answers_df, on="Question ID", how="left")

        # Calculate accuracy score
        data_with_answers["Accuracy Score"] = data_with_answers.apply(
            lambda row: 1 if row["Answer"] == row["Correct Answer"]
            else (0.5 if pd.notna(row["Answer"]) else 0),
            axis=1
        )

        # Prepare input data for prediction
        X = pd.get_dummies(data_with_answers[["Quiz ID", "Topic", "Answer"]])

        # Align input features with model's expected features
        X = X.reindex(columns=model_features, fill_value=0)

        # Make predictions
        data_with_answers["Predicted"] = model.predict(X)

        # Calculate performance and topics to review
        performance = data_with_answers.groupby("Topic")["Accuracy Score"].mean().reset_index()
        performance.columns = ["Topic", "Average Accuracy"]

        threshold = 0.7  # Define the threshold for topics to review
        to_review = performance[(performance["Average Accuracy"] < threshold) & (performance["Average Accuracy"] > 0)]

        # Identify wrong answers
        wrong_answers = data_with_answers[data_with_answers["Accuracy Score"] == 0.5][
            ["Question ID", "Question", "Topic", "Answer", "Correct Answer"]
        ]

        # Calculate model accuracy based on predictions
        correct_predictions = (
            data_with_answers["Predicted"] == (data_with_answers["Accuracy Score"] == 1)
        ).mean() * 100

        # Prepare response
        output = {
            "Model Accuracy": f"{correct_predictions:.2f}%",
            "Wrong Answers": wrong_answers.to_dict(orient="records"),
            "Topics to Review": to_review.to_dict(orient="records"),
        }
        return jsonify(output)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
