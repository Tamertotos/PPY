import data
from question_model import Question
from quiz_app import Quiz

question_dictionary = data.get_questions_api("https://opentdb.com/api.php")
question_bank = [Question(question_dictionary[i]["question"], question_dictionary[i]["correct_answer"])  for i in range(len(question_dictionary))]

quiz = Quiz(question_bank)

while quiz.has_next():
    quiz.next_question()