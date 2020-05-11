from pygame import init
import threading
import atexit
from tkinter import *
from emotion_classifier import emotion_recognition, cap
from static_ui import raise_frame, start_frame, window
from music_player import MusicPlayer
from dynamic_ui import DynamicUI
from game_state import GameState
from emotion_map import EmotionMap


if __name__ == '__main__':
    init()

    raise_frame(start_frame)
    dui = DynamicUI()
    mp = MusicPlayer()
    em = EmotionMap(dui, mp)

    e = threading.Event()
    x = threading.Thread(target=emotion_recognition, args=(e, dui))
    gs = GameState(x, e, dui, mp, em)

    start_emotion_button = Button(start_frame, text="Start Emotion Recognition", height=2,
                                  command=gs.start).grid(row=2, column=0, columnspan=2, sticky=N+S+W+E)
    quit_button = Button(start_frame, text="Exit", height=2,
                         command=gs.quit_app).grid(row=3, column=0, columnspan=2, sticky=N+S+W+E)

    gs.reset_frame()
    window.mainloop()


def release():
    cap.release()


atexit.register(release)
