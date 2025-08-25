# main.py
from gui import QuizGUI
from quiz_data import get_questions, calculate_score, get_feedback

class QuizGameController:
    def __init__(self):
        self.player_name = ""
        self.topic = ""
        self.questions = []
        self.current_q = 0
        self.selected_answers = []
        self.selected_option = None
        self.gui = QuizGUI(self.start_quiz_callback, self.restart_quiz)

    def start_quiz_callback(self, mode=None):
        if mode == "get_topics":
            return list(get_questions().keys())  # 🔄 Fetch fresh topics from shuffled data

        self.player_name = self.gui.get_player_name()
        self.topic = self.gui.get_selected_topic()
        if not self.player_name or not self.topic:
            self.gui.show_warning("Please enter your name and select a topic!")
            return

        self.questions_bank = get_questions()  # 🔄 Fetch fresh randomized questions
        self.questions = self.questions_bank[self.topic]
        self.current_q = 0
        self.selected_answers = []
        import tkinter as tk
        self.selected_option = tk.StringVar()
        self.show_question()

    def show_question(self):
        def on_next():
            if not self.selected_option.get():
                self.gui.show_warning("Please select an answer before proceeding!")
                return
            self.selected_answers.append(self.selected_option.get())
            self.current_q += 1
            if self.current_q < len(self.questions):
                self.show_question()
            else:
                self.show_result()
        self.gui.show_question(self.player_name, self.topic, self.questions, self.current_q, self.selected_option, on_next)

    def show_result(self):
        score = calculate_score(self.selected_answers, self.questions)
        feedback = get_feedback(score, len(self.questions))
        self.gui.show_result(self.player_name, self.topic, score, len(self.questions), feedback)

    def restart_quiz(self):
        self.player_name = ""
        self.topic = ""
        self.questions = []
        self.current_q = 0
        self.selected_answers = []
        self.gui.create_start_screen()

if __name__ == "__main__":
    game = QuizGameController()
    game.gui.run()
