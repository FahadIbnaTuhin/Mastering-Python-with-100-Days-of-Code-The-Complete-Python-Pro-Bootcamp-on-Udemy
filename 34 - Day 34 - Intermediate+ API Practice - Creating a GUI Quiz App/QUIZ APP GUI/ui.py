from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # quiz_brain: QuizBrain --> quizBrain r vitorer method jate ekhane dekhte pari, tai emon korsi
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Solve Questions")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Are you ready to solve?",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=25)

        ok_pic = PhotoImage(file="images/true.png")
        self.okBtn = Button(image=ok_pic, highlightthickness=0, command=self.true_pressed)
        self.okBtn.grid(row=2, column=0)

        cancel_pic = PhotoImage(file="images/false.png")
        self.cancelBtn = Button(image=cancel_pic, highlightthickness=0, command=self.false_pressed)
        self.cancelBtn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.okBtn.config(state="disabled")
            self.cancelBtn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
