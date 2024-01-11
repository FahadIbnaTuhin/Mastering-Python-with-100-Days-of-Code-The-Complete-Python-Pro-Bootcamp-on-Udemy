class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # directly show true if the condition is true. can use return if inside "if" you return true and outside false
        # if self.question_number < len(self.question_list):
        #     return True
        # return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_ans, c_ans):
        if u_ans.lower() == c_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct ans was {c_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
