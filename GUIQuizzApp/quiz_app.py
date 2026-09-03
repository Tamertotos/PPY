
class Quiz:

    def __init__(self, question_list):
        self.current_question_number = 0
        self.score = 0
        self.questions: list = question_list

    def has_next(self):
        return len(self.questions) - 1 > self.current_question_number

    def next_question(self,state):
        self.check_answer(state, self.questions[self.current_question_number].answer.lower())
        self.current_question_number += 1

    def check_answer(self,user_answer,answer_to_question):
        if user_answer == answer_to_question:
            self.score += 1


