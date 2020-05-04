from tkinter import *
import random
from static_ui import ai_frame, raise_frame


class EmotionMap:
    def __init__(self, dui, mp):
        self.dui = dui
        self.mp = mp

    def map_emotion(self, emotion):
        self.dui.frame_stream(emotion)
        if emotion == 'Sad':
            self.map_to_sad()
        elif emotion == 'Angry':
            self.map_to_angry()
        elif emotion == 'Happy':
            self.map_to_happy()
        elif emotion == 'Surprise':
            self.map_to_surprised()
        raise_frame(ai_frame)

    def map_to_surprised(self):
        fact = self.surprised()
        self.dui.set_emotion_title('Did You Know?!')
        reaction_text = Label(ai_frame, text=fact, anchor=CENTER, background="black", font=("Helvetica", 14),
                              fg="white", width=100, height=2).grid(row=2, column=0, columnspan=2, sticky=N + S + W + E)
        another_fact_button = Button(ai_frame, text="Another one, Please!", height=2, width=26,
                                     command=lambda: self.map_emotion('Surprise')).grid(row=3, column=0, columnspan=2,
                                                                                        sticky=N + S + W + E)

    def map_to_sad(self):
        joke = self.sad()
        self.dui.set_emotion_title('Laughter is the Best Medicine')
        reaction_text = Label(ai_frame, text=joke, anchor=CENTER, background="black", font=("Helvetica", 14),
                              fg="white", width=100, height=2).grid(row=2, column=0, columnspan=2, sticky=N + S + W + E)
        another_joke_button = Button(ai_frame, text="Another one, Please!", height=2, width=26,
                                     command=lambda: self.map_emotion('Sad')).grid(row=3, column=0, columnspan=2,
                                                                                   sticky=N + S + W + E)

    def map_to_angry(self):
        self.dui.set_emotion_title('Take A Deep Breath')
        textfile = 'reactions/reaction_angry/songs.txt'
        reaction_path = 'reactions/reaction_angry/'
        self.mp.get_song(reaction_path, textfile)
        self.mp.set_music_ui()

    def map_to_happy(self):
        self.dui.set_emotion_title('Party Time!')
        textfile = 'reactions/reaction_happy/songs.txt'
        reaction_path = 'reactions/reaction_happy/'
        self.mp.get_song(reaction_path, textfile)
        self.mp.set_music_ui()

    def get_from_file(self, path):
        line = open(path).read().splitlines()
        return random.choice(line)

    def sad(self):
        path = 'reactions/reaction_sad/jokes.txt'
        return self.get_from_file(path)

    def surprised(self):
        path = 'reactions/reaction_surprised/facts.txt'
        return self.get_from_file(path)
