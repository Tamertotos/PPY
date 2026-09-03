import data
from question_model import Question

question_dictionary = data.get_questions_api("https://opentdb.com/api.php")
question_bank = [Question(question_dictionary[i]["question"], question_dictionary[i]["correct_answer"])  for i in range(len(question_dictionary))]

print(question_bank[0])