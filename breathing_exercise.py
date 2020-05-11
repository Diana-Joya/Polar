from tkinter import *
from static_ui import ai_frame, window


class BreathingExercise:
    def __init__(self, dui):
        # Countdown Settings
        self.dui = dui
        self.remaining = 0
        self.time = 4
        self.state = 0

    def relax_countdown(self, label, action):
        if self.dui.current == 'Angry':
            if self.time is not None:
                self.remaining = self.time
            if self.remaining <= 0:
                text = "Time's up! You did it!"
                self.dui.set_emotion_title(text)
                self.dui.ai_frame_stream(label, action)
            else:
                if self.state == 0 or self.state == 1:
                    self.get_started()
                    self.state += 1
                elif self.state == 2:
                    self.breathe_in()
                elif self.state == 3:
                    self.hold_breath()
                elif self.state == 4:
                    self.exhale()
                self.remaining -= 1
                self.time -= 1
                window.after(1000, lambda: self.relax_countdown(label, action))

    def get_started(self):
        if self.state == 0:
            text = "Let do some breathing exercises!"
        else:
            text = "Ready?"
        self.time = 5
        self.dui.set_emotion_title(text)

    def breathe_in(self):
        text = "Breathe in quietly through the nose for {remaining} seconds".format(remaining=self.remaining)
        self.dui.set_emotion_title(text)
        if self.time == 1:
            self.time = 8
            self.state += 1

    def hold_breath(self):
        text = "Gently hold your breath for {remaining} seconds".format(remaining=self.remaining)
        self.dui.set_emotion_title(text)
        if self.time == 1:
            self.time = 9
            self.state += 1

    def exhale(self):
        text = "Exhale through your mouth for {remaining} seconds".format(remaining=self.remaining)
        self.dui.set_emotion_title(text)
