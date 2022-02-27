
# TODO: ask questions
# TODO: check if answer given is correct
# TODO: check if we are already at the end of the quiz
class QuizBrain:
    def __init__(self, question_list):
        self.quiz_list = question_list
        self.question_number = 0

    def next_question(self):
        current_question = self.quiz_list[self.question_number]
        input(f"Q.{self.question_number}: {current_question.text} (True or False): ")

