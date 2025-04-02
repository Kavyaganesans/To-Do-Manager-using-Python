""" It is a simple trivia game that asks the user 5 questions from a predefined set of questions."""
# The user has to answer the questions, and at the end, their score is displayed.
import random
questions ={
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "What is the chemical symbol for gold?": "Au",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the smallest prime number?": "2",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the freezing point of water in Celsius?": "0",
    "What is the square root of 16?": "4",
    "What is the capital of Japan?": "Tokyo",
    "What is the longest river in the world?": "Nile",
    "What is the main ingredient in guacamole?": "Avocado",
    "What is the hardest natural substance on Earth?": "Diamond",
    "What is the chemical formula for water?": "H2O",
    "What is the largest desert in the world?": "Sahara Desert",
    "What is the currency of the United States?": "Dollar",
}
# questions["What is 2 + 2?"] >> "4"
# questions["What is the capital of France?"] >> "Paris"

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 10
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    print("Lets start with some basic aptitude questions")
    print("You will be asked 5 questions. Try to answer them correctly!")
    print("Let's start!")

    for idx , question in enumerate(selected_questions):
        print(f"{idx+1}.{question}")
        user_answer=input("Your answer:").strip().lower()
        correct_answer = questions[question].strip().lower()
        if user_answer == correct_answer:
            print("Correct! \n")
            score +=1
        else:
            print(f"Wrong! The correct answer is: {questions[question]} \n") 

    print(f"Your final score is {score}/{total_questions}.")                         
python_trivia_game()