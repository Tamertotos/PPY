
class Quiz:

    def __init__(self, question_list):
        self.current_question_number = 0
        self.score = 0
        self.questions: list = question_list

    def has_next(self) -> bool:
        return len(self.questions) - 1 > self.current_question_number

    def next_question(self):
        self.current_question_number += 1

    def check_answer(self,user_answer) -> str:
        print(self.questions[self.current_question_number].answer)
        if user_answer == self.questions[self.current_question_number].answer.lower():
            self.score += 1
            return "green"
        else:
            return "red"

