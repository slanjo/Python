#This Class is/Will be:
# TODO - askting the questions 
# TODO - checking if the answer was correct
# TODO - checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        ### Retreive the item at the current question_number from the question_list. ###
        current_question = self.question_list[self.question_number] 
        self.question_number += 1
        input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")
