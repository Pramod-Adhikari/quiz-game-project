import tkinter as tk
from tkinter import messagebox

class QuizGUI:
    def __init__(self, start_quiz_callback, restart_callback):
        self.root = tk.Tk()
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.bg_base = "#f2f2f2"
        self.root.configure(bg=self.bg_base)
        self.start_quiz_callback = start_quiz_callback
        self.restart_callback = restart_callback
        self.timer_active = False

    # FADE-IN ANIMATION
    def fade_in(self, widget, step=0, max_steps=10):
        color = self._fade_color(step, max_steps)
        self.root.configure(bg=color)
        widget.configure(bg=color)
        if step < max_steps:
            self.root.after(30, lambda: self.fade_in(widget, step+1, max_steps))

    def _fade_color(self, step, max_steps):
        white_rgb = self.root.winfo_rgb("#ffffff")
        base_rgb = self.root.winfo_rgb(self.bg_base)
        r = int(white_rgb[0] + (base_rgb[0] - white_rgb[0]) * step / max_steps) // 256
        g = int(white_rgb[1] + (base_rgb[1] - white_rgb[1]) * step / max_steps) // 256
        b = int(white_rgb[2] + (base_rgb[2] - white_rgb[2]) * step / max_steps) // 256
        return f'#{r:02x}{g:02x}{b:02x}'

    def run(self):
        self.create_start_screen()
        self.root.mainloop()

    def create_start_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root, bg=self.bg_base)
        frame.pack(fill='both', expand=True)
        self.fade_in(frame)
        tk.Label(frame, text="Welcome to Quiz Game!", font=("Arial", 18, "bold"), bg=self.bg_base, fg="#333").pack(pady=20)
        tk.Label(frame, text="Enter your name:", font=("Arial", 12), bg=self.bg_base).pack(pady=5)
        self.name_entry = tk.Entry(frame, font=("Arial", 12), justify="center")
        self.name_entry.pack(pady=5)
        tk.Label(frame, text="Choose Topic:", font=("Arial", 12), bg=self.bg_base).pack(pady=10)
        self.topic_var = tk.StringVar()
        self.topic_buttons = []
        for topic in self.start_quiz_callback("get_topics"):
            btn = tk.Radiobutton(frame, text=topic, variable=self.topic_var, value=topic, font=("Arial", 11), bg=self.bg_base, anchor="w")
            btn.pack(pady=2)
            self.topic_buttons.append(btn)
        tk.Button(frame, text="Start Quiz", command=self._start_quiz, bg="#4caf50", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    def _start_quiz(self):
        self.start_quiz_callback()

    # SLIDE-IN ANIMATION FOR QUESTION
    def show_question(self, player_name, topic, questions, current_q, selected_option, on_next, timer_seconds=30):
        self.clear_screen()
        self.timer_active = False  # Stop any previous timer loop
        frame = tk.Frame(self.root, bg=self.bg_base)
        frame.place(x=-500, y=0, width=500, height=400)
        self._slide_in(frame)

        q_data = questions[current_q]
        tk.Label(frame, text=f"{topic} Quiz", font=("Arial", 16, "bold"), bg=self.bg_base, fg="#0077b6").pack(pady=10)
        tk.Label(frame, text=f"Player: {player_name}", font=("Arial", 12), bg=self.bg_base).pack()
        tk.Label(frame, text=f"Question {current_q + 1}/{len(questions)}", font=("Arial", 12), bg=self.bg_base).pack(pady=5)
        tk.Label(frame, text=q_data["q"], font=("Arial", 13), wraplength=400, bg=self.bg_base).pack(pady=10)
        selected_option.set(None)
        for opt in q_data["options"]:
            tk.Radiobutton(frame, text=opt, variable=selected_option, value=opt, font=("Arial", 12), bg=self.bg_base).pack(anchor="w", padx=80)

        self.remaining = timer_seconds
        self.timer_label = tk.Label(frame, text=f"Time left: {self.remaining}s", font=("Arial", 12), bg=self.bg_base, fg="#e53935")
        self.timer_label.pack()
        self.timer_active = True

        def next_and_stop_timer():
            self.timer_active = False
            on_next()

        tk.Button(frame, text="Next", command=next_and_stop_timer, bg="#2196f3", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
        self._update_timer(next_and_stop_timer)

    def _slide_in(self, frame, x=-500, target_x=0, step=20):
        if x < target_x:
            frame.place(x=x, y=0)
            self.root.after(10, lambda: self._slide_in(frame, x+step, target_x, step))
        else:
            frame.place(x=target_x, y=0)

    def _update_timer(self, on_next):
        if not self.timer_active:
            return  # Prevent overlapping timers

        if self.remaining > 0:
            self.timer_label.config(text=f"Time left: {self.remaining}s")
            self.remaining -= 1
            self.root.after(1000, lambda: self._update_timer(on_next))
        else:
            self.timer_active = False
            on_next()

    def show_result(self, player_name, topic, score, total, feedback):
        self.clear_screen()
        frame = tk.Frame(self.root, bg=self.bg_base)
        frame.pack(fill='both', expand=True)
        self.fade_in(frame)
        tk.Label(frame, text="Quiz Completed!", font=("Arial", 18, "bold"), bg=self.bg_base, fg="#4caf50").pack(pady=30)
        tk.Label(frame, text=f"Player: {player_name}", font=("Arial", 13), bg=self.bg_base).pack()
        tk.Label(frame, text=f"Topic: {topic}", font=("Arial", 13), bg=self.bg_base).pack()
        tk.Label(frame, text=f"Score: {score} / {total}", font=("Arial", 16, "bold"), bg=self.bg_base, fg="#333").pack(pady=10)
        tk.Label(frame, text=feedback, font=("Arial", 12, "italic"), bg=self.bg_base, fg="#880e4f").pack(pady=5)
        tk.Button(frame, text="Restart", command=self.restart_callback, bg="#ff9800", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
        tk.Button(frame, text="Exit", command=self.root.quit, bg="#e53935", fg="white", font=("Arial", 12, "bold")).pack()

    def show_warning(self, msg):
        messagebox.showwarning("Input Error", msg)

    def get_player_name(self):
        return self.name_entry.get()

    def get_selected_topic(self):
        return self.topic_var.get()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
