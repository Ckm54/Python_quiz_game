from question_model import Question
from data import question_data

question_database = []
for question in question_data:
    quiz_text = question["text"]
    quiz_answer = question["answer"]
    new_question = Question(quiz_text, quiz_answer)
    question_database.append(new_question)



