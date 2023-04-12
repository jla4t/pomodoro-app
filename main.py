from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
main_window = Tk()
BG_IMAGE = PhotoImage(file="tomato.png")
REPS = 0
TIMER = None
# Special Characters Used: ✔
# Take One! ✔✔✔✔✔✔✔✔
checkmarks = []


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global REPS
    global TIMER
    global checkmarks
    main_window.after_cancel(TIMER)
    bg.itemconfig(timer_text, text="00:00")
    top_text.config("Session Reset.")
    REPS = 0
    checkmarks = []


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS == 8:
        count_down(LONG_BREAK_MIN * 60)
        top_text.config(text="Well done! Break time.", fg=RED)
        REPS = 0
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        top_text.config(text="Take a break!", fg=RED)
        checkmarks.append("✔")
    else:
        count_down(WORK_MIN * 60)
        top_text.config(text="Time to work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_allotted):
    global TIMER
    sec = time_allotted % 60
    if sec < 10:
        sec = f"0{sec}"
    min = math.floor(time_allotted/60)
    time_output = f"{min}:{sec}"
    bg.itemconfig(timer_text, text=time_output)
    if time_allotted > 0:
        TIMER = main_window.after(1000, count_down, time_allotted - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
main_window.title("Pomodoro Timer")
main_window.config(padx=100, pady=50, bg=YELLOW)

top_text = Label(text="Pomodoro Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
top_text.grid(column=1, row=0)

bg = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg.create_image(100, 110, image=BG_IMAGE)
timer_text = bg.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
bg.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), bg=YELLOW, command=start_timer)
start_button.config(highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 16, "bold"), bg=YELLOW, command=timer_reset)
reset_button.config(highlightthickness=0)
reset_button.grid(column=2, row=2)

tracker = Label(text=checkmarks, bg=YELLOW, fg=GREEN, highlightthickness=0)
tracker.grid(column=1, row=3)

main_window.mainloop()
