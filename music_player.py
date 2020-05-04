from pygame import mixer
from tkinter import *
import random
from static_ui import ai_frame


class MusicPlayer:
    def __init__(self):
        self.sound_playing = False
        self.path = ''

    def get_song(self, reaction_path, textfile):
        songs = open(textfile).read().splitlines()
        song = random.choice(songs)
        self.path = reaction_path + song + ".mp3"
        self.play_music()

    def play_music(self):
        mixer.music.unload()
        print('Now Playing: ', self.path)
        mixer.music.load(self.path)
        mixer.music.play()
        self.sound_playing = True

    def stop_music(self):
        mixer.music.stop()
        self.sound_playing = False

    def pause_music(self):
        mixer.music.pause()
        self.sound_playing = False

    def resume_music(self):
        mixer.music.unpause()
        self.sound_playing = True

    def set_music_ui(self):
        play_music_button = Button(ai_frame, text="Play", height=2, width=26,
                                   command=self.play_music).grid(row=2, column=0, sticky=N + S + W + E)
        stop_music_button = Button(ai_frame, text="Stop", height=2, width=26,
                                   command=self.stop_music).grid(row=2, column=1, sticky=N + S + W + E)
        pause_music_button = Button(ai_frame, text='pause', height=2, width=26,
                                    command=self.pause_music).grid(row=3, column=0, sticky=N + S + W + E)
        resume_music_button = Button(ai_frame, text='resume', height=2, width=26,
                                     command=self.resume_music).grid(row=3, column=1, sticky=N + S + W + E)
