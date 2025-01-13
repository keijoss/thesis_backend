from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load your trained model
model = pickle.load(open("dataset/male_quiz_ai.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/male', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        input_data = request.get_json(force=True)
        student_answers = input_data['answers']  # Ensure the key matches your client-side structure

        # Validate the input
        if not isinstance(student_answers, list) or not student_answers:
            return jsonify({"error": "Invalid input format. 'answers' must be a non-empty list."}), 400

        # Convert student answers into DataFrame
        answers_df = pd.DataFrame(student_answers)

        # Load dataset with questions and answers
        dataset = pd.read_pickle("dataset/questions_male.pkl")  # Save your question dataset to this file
        data = dataset.merge(answers_df, on="Question ID", how="left")

        # Add 'Is Correct' column
        data["Is Correct"] = (data["Answer"] == data["Correct Answer"]).astype(int)

        # # Prepare data for prediction
        # X = pd.get_dummies(data[["Quiz ID", "Topic", "Answer"]])

        # # Predict using the loaded model
        # data["Predicted"] = model.predict(X)

        # Prepare data for prediction
        X = pd.get_dummies(data[["Quiz ID", "Topic", "Answer"]])

        # Debugging: Check the input to the model
        print("Input to model:", X.head())

        # Predict using the loaded model
        try:
            data["Predicted"] = model.predict(X.values)
        except Exception as e:
            print(f"Error during prediction: {e}")
            return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

        # Calculate performance by topic
        performance = data.groupby("Topic")["Is Correct"].mean().reset_index()
        performance.columns = ["Topic", "Accuracy"]

        # Suggest topics for review
        threshold = 0.7
        to_review = performance[performance["Accuracy"] < threshold]

        # Model accuracy
        overall_accuracy = (data["Predicted"] == data["Is Correct"]).mean()

        # Response payload
        response = {
            "overall_accuracy": f"{overall_accuracy * 100:.2f}%",
            "topics_to_review": to_review.to_dict(orient="records")
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
