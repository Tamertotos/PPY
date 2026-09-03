import html

class Quiz:

    def __init__(self, question_list):
        self.current_question_number = 0
        self.score = 0
        self.questions: list = question_list

    def has_next(self):
        return len(self.questions) > self.current_question_number

    def next_question(self):
        q_text = html.unescape(self.questions[self.current_question_number].text)
        user_answer = input(f"Q.{self.current_question_number} {q_text}. (True/False):").lower()
        self.check_answer(user_answer, self.questions[self.current_question_number].answer)
        self.current_question_number += 1

    def check_answer(self,user_answer,answer_to_question):
        if user_answer == answer_to_question:
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect!")
        print(f"The correct answer was {answer_to_question}.")
        print(f"Your current score is {self.score}/{self.current_question_number+1}.\n")

