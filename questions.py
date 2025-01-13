import pandas as pd

# Define the questions data
questions_data = [
    {"Quiz ID": "Quiz 1", "Question ID": "M1", "Question": "What is the primary function of the prostate gland?",
     "Options": "a. Store urine, b. Produce seminal fluid, c. Protect the kidneys, d. Regulate hormones",
     "Correct Answer": "b", "Topic": "Prostate Gland"},
    {"Quiz ID": "Quiz 1", "Question ID": "M2", "Question": "Which part of the male reproductive system is responsible for carrying urine and semen out?",
     "Options": "a. Bladder, b. Urethra, c. Penis, d. Prostate gland",
     "Correct Answer": "b", "Topic": "Urethra"},
    {"Quiz ID": "Quiz 1", "Question ID": "M3", "Question": "What is the role of the spermatic cord?",
     "Options": "a. To transport sperm and blood to the testes, b. To produce testosterone, c. To store urine, d. To filter blood",
     "Correct Answer": "a", "Topic": "Spermatic Cord"},
    {"Quiz ID": "Quiz 1", "Question ID": "M4", "Question": "What is the function of the testes?",
     "Options": "a. To produce and store sperm, b. To regulate blood flow, c. To store urine, d. To produce seminal fluid",
     "Correct Answer": "a", "Topic": "Testes"},
    {"Quiz ID": "Quiz 1", "Question ID": "M5", "Question": "Which organ is responsible for producing testosterone in males?",
     "Options": "a. Prostate gland, b. Testes, c. Kidney, d. Bladder",
     "Correct Answer": "b", "Topic": "Testes"},
    {"Quiz ID": "Quiz 1", "Question ID": "M6", "Question": "What is the primary function of the bladder?",
     "Options": "a. To produce sperm, b. To store urine, c. To produce seminal fluid, d. To transport sperm",
     "Correct Answer": "b", "Topic": "Bladder"},
    {"Quiz ID": "Quiz 1", "Question ID": "M7", "Question": "What is the function of the penis in the male reproductive system?",
     "Options": "a. To produce sperm, b. To deliver sperm into the female reproductive system, c. To regulate hormone production, d. To filter blood",
     "Correct Answer": "b", "Topic": "Penis"},
    {"Quiz ID": "Quiz 1", "Question ID": "M8", "Question": "What are the tiny tubes in the testes where sperm production occurs called?",
     "Options": "a. Urethra, b. Seminiferous tubules, c. Vas deferens, d. Epididymis",
     "Correct Answer": "b", "Topic": "Testes"},
    {"Quiz ID": "Quiz 1", "Question ID": "M9", "Question": "Where is sperm stored before ejaculation?",
     "Options": "a. Prostate gland, b. Vas deferens, c. Epididymis, d. Urethra",
     "Correct Answer": "c", "Topic": "Epididymis"},
    {"Quiz ID": "Quiz 1", "Question ID": "M10", "Question": "Which part of the male reproductive system transports sperm from the testes to the urethra?",
     "Options": "a. Vas deferens, b. Prostate gland, c. Seminiferous tubules, d. Bladder",
     "Correct Answer": "a", "Topic": "Vas Deferens"}
]

# Convert to a pandas DataFrame
questions_df = pd.DataFrame(questions_data)

# Save the DataFrame to a pickle file
questions_df.to_pickle("dataset/questions_male.pkl")
print("Questions dataset saved as 'dataset/questions.pkl'")
