from tkinter import *
from ui import Ui
from get_words import GetWords

first_letter = True
content_count = 1
current_word_count = 0
TIMER = 30
CORRECT = 0
WRONG = 0
after_id = ""


# ---------------------- Start timer when user starts typing ---------------------
def get_key(key):
    global first_letter
    if first_letter:
        first_letter = False
        update_timer(TIMER)
    compare(key.char)


# -------------------------------- Update Timer-------------------------------
def update_timer(count):
    global after_id
    ui.time_label.config(text=count)
    if count > 0:
        after_id = window.after(1000, update_timer, count - 1)
    else:
        speed_accuracy()


# ----------------------------------------------------------------------------


# -------------------------------- Compare text -----------------------------------
def compare(user_letter):
    global content_count
    global current_word_count
    global CORRECT, WRONG
    ui.text.tag_configure("green", foreground="green")
    ui.text.tag_configure("red", foreground="red")
    if user_letter == " ":

        if ui.text.get(f"{content_count}.{current_word_count}") == " ":
            current_word_count += 1
        else:
            next_space_index = ui.text.search(
                " ", f"{content_count}.{current_word_count + 1}"
            )

            if next_space_index != -1:
                current_word_count = int(next_space_index.split(".")[1]) + 1
    else:
        current_index_count = f"{content_count}.{current_word_count}"
        actual_letter = ui.text.get(current_index_count)
        # print(f"Acutal: {actual_letter}, User: {user_letter}")
        if actual_letter == user_letter:
            ui.text.tag_add("green", current_index_count)
            CORRECT += 1
        else:
            ui.text.tag_add("red", current_index_count)
            WRONG += 1
        current_word_count += 1


# -------------------------------------------------------------------------------------
def backspace_pressed(key):
    global content_count, current_word_count, CORRECT, WRONG
    current_word_count -= 1
    current_index = f"{content_count}.{current_word_count}"
    if ui.text.get(current_index) == " ":
        pass
    else:
        tag_name = ui.text.tag_names(current_index)[1]
        if tag_name.lower() == "green":
            CORRECT -= 1
        else:
            WRONG -= 1
        ui.text.tag_remove(tag_name, current_index)


# ---------------------------- Calculate speed and accuracy -----------------------------
def speed_accuracy():
    global CORRECT, WRONG
    final_window = Tk()
    final_window.config(padx=50, pady=50)
    try:
        speed = ((CORRECT + WRONG) / 5 - WRONG) / 0.5
        accuracy = (CORRECT / (CORRECT + WRONG)) * 100
    except ZeroDivisionError:
        speed = 0
        accuracy = 0
    speed = round(speed, 2)
    accuracy = round(accuracy, 2)
    print(f"Speed: {speed} words per minute \n Accuracy: {accuracy}%")
    speed_label = Label(final_window, text=f"Speed: {speed} WPM")
    speed_label.pack()
    accuracy_label = Label(final_window, text=f"Accuracy: {accuracy}%")
    accuracy_label.pack()
    final_window.mainloop()


# -------------------------------------------------------------------------------


# ------------------------------------------Reset--------------------------------------
def reset():
    window.after_cancel(after_id)
    ui.time_label.config(text="30")
    ui.user_text.delete(0, END)
    ui.text.tag_remove("green", "1.0", END)
    ui.text.tag_remove("red", "1.0", END)
    global current_word_count, first_letter, CORRECT, WRONG
    first_letter = True
    current_word_count = 0
    CORRECT = 0
    WRONG = 0
    get_words.text = ""
    get_words.get_200_words()
    ui.place_text(
        get_words.text,
        window,
    )


window = Tk()
window.config(padx=200, pady=100, bg="black")
ui = Ui()
get_words = GetWords()
get_words.get_200_words()

ui.place_welcome_label()
ui.place_time_label()
ui.place_text(
    get_words.text,
    window,
)
ui.place_user_text()
ui.place_restart_button()
ui.user_text.bind("<Key>", get_key)
ui.user_text.bind("<BackSpace>", backspace_pressed)
ui.restart_button.config(command=reset)
window.mainloop()
