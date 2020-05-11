from tkinter import *
import random
from static_ui import ai_frame, raise_frame
from breathing_exercise import BreathingExercise


class EmotionMap:
    def __init__(self, dui, mp):
        self.dui = dui
        self.mp = mp
        self.be = BreathingExercise(dui)

    def map_emotion(self, emotion):
        self.dui.frame_stream(emotion)
        if emotion == 'Sad':
            self.map_to_sad(emotion)
        elif emotion == 'Angry':
            self.map_to_angry(emotion)
        elif emotion == 'Happy':
            self.map_to_happy(emotion)
        elif emotion == 'Surprise':
            self.map_to_surprised(emotion)
        raise_frame(ai_frame)

    def map_to_surprised(self, emotion):
        path = 'reactions/reaction_surprised/facts.txt'
        fact, reaction = self.text_based(path)
        self.dui.set_emotion_title('Did You Know?!')
        self.dui.ai_frame_stream(emotion, reaction)
        self.dui.set_speech_bubble(fact)
        another_fact_button = Button(ai_frame, text="Another one, Please!", height=2, width=26,
                                     command=lambda: self.map_emotion(emotion)).grid(row=2, column=0, columnspan=2,
                                                                                     rowspan=2, sticky=N + S + W + E)

    def map_to_sad(self, emotion):
        path = 'reactions/reaction_sad/jokes.txt'
        joke, reaction = self.text_based(path)
        self.dui.set_emotion_title('Laughter is the Best Medicine')
        self.dui.ai_frame_stream(emotion, reaction)
        self.dui.set_speech_bubble(joke)
        another_joke_button = Button(ai_frame, text="Another one, Please!", height=2, width=26,
                                     command=lambda: self.map_emotion(emotion)).grid(row=2, column=0, columnspan=2,
                                                                                     rowspan=2, sticky=N + S + W + E)

    def map_to_angry(self, emotion):
        self.dui.set_emotion_title("Let's Take a Deep Breath!")
        self.dui.ai_frame_stream(emotion, 'Relaxing')
        self.be.state = 0
        self.be.relax_countdown(emotion, 'Relaxed')
        textfile = 'reactions/reaction_angry/songs.txt'
        reaction_path = 'reactions/reaction_angry/'
        self.mp.get_song(reaction_path, textfile)

    def map_to_happy(self, emotion):
        self.dui.set_emotion_title('Party Time!')
        self.dui.ai_frame_stream(emotion, 'Party')
        textfile = 'reactions/reaction_happy/songs.txt'
        reaction_path = 'reactions/reaction_happy/'
        self.mp.get_song(reaction_path, textfile)

    def get_from_file(self, path):
        line = open(path).read().splitlines()
        return random.choice(line)

    def text_based(self, path):
        line = self.get_from_file(path)
        split = line.split(':')
        return split[0], split[1]
