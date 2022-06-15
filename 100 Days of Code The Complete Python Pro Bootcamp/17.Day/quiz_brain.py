from typing_extensions import Self


class QuizBrain():
    def __init__(self,question_number,question_list):
        self.question_number = 0
        self.list = question_list

    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        input(f"Q.{current_question}:{current_question.text}(True/False)")


