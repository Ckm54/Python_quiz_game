from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_database = []
for question in question_data:
    quiz_text = question["text"]
    quiz_answer = question["answer"]
    new_question = Question(quiz_text, quiz_answer)
    question_database.append(new_question)

quiz = QuizBrain(question_database)
quiz.next_question()

