class Question():
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

p1 = Question("2+3=5","True")
print(p1.answer)