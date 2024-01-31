from tkinter import *


class Ui:
    def __init__(self):
        self.welcome_label = Label()
        self.time_label = Label()
        self.text = None
        self.user_text = Entry()
        self.restart_button = Button()

    def place_welcome_label(self):
        self.welcome_label.config(
            text="Welcome to Typing Speed Test",
            background="black",
            foreground="white",
            font=("Arial", 13, "bold"),
        )
        self.welcome_label.grid(row=0, column=1, sticky="w", pady=25)

    def place_time_label(self):
        self.time_label.config(
            text="30",
            background="black",
            foreground="white",
            font=("Arial", 13, "bold"),
        )
        self.time_label.grid(row=0, column=0, sticky="w", pady=25)

    def place_text(self, text, window):
        self.text = Text(window, height=10)
        self.text.config(
            background="black",
            foreground="white",
            font=("Arial Rounded MT", 12, "bold"),
            padx=10,
            pady=15,
        )
        text = text.lower()
        self.text.insert(END, text, "center")
        # self.text.tag_config("center", justify=CENTER)
        self.text.config(state="disabled")
        self.text.grid(row=1, column=0, columnspan=2)

    def place_user_text(self):
        self.user_text.config(width=40, font=("Arial", 15))
        self.user_text.grid(row=3, column=0, columnspan=2, pady=25)

    def place_restart_button(self):
        self.restart_button.config(text="Reset")
        self.restart_button.grid(row=4, column=0, pady=25, columnspan=2)
