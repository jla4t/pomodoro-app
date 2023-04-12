Pomodoro Timer Application

This is a Python-based Pomodoro Timer application that uses the Tkinter library for the graphical user interface (GUI). The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s, which uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

Features

    Countdown timer with adjustable duration
    Start and reset buttons for controlling the timer
    Timer shown to visualize the time remaining
    Option to customize the application settings, such as the timer durations

Requirements

    Python 3.x
    Tkinter (Python's standard GUI library)

Installation

    Clone the repository or download the source code.

Usage

    Click the "Start" button to begin the Pomodoro Timer.
    The timer will count down the work duration for each part of the session.
    When the work duration ends, the short break duration will start automatically.
    After the short break, the timer will reset and start counting down the work duration again.
    After completing a set number of work durations, the long break duration will start instead of the short break.
    Reset the timer using the reset button as needed.

Customization

You can customize the timer settings by changing the default values in the pomodoro_timer.py script. For example, you can adjust the default work duration, short break duration, and long break duration (x, y, and z)

# Timer settings
    WORK_MIN = x * 60
    SHORT_BREAK_MIN = y * 60
    LONG_BREAK_MIN = z * 60

Contributing

If you would like to contribute to this Pomodoro Timer application, feel free to submit a pull request with your improvements or open an issue for any bug reports or feature requests.

License

This Pomodoro Timer application is released under the MIT License, which allows for free use, modification, and distribution of the code. Please refer to the LICENSE file for more details.

Credits

This Pomodoro Timer application was created by Jean-Luc Affourtit and is based on the Pomodoro Technique developed by Francesco Cirillo. It uses the Tkinter library for the GUI.
