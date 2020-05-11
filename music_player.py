from pygame import mixer
from tkinter import *
import random
from static_ui import ai_frame


class MusicPlayer:
    def __init__(self):
        self.sound_playing = False
        self.paused = False
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
        self.set_music_ui()

    def stop_music(self):
        mixer.music.stop()
        self.sound_playing = False
        self.set_music_ui()

    def pause_music(self):
        mixer.music.pause()
        # self.sound_playing = False
        self.paused = True
        self.set_music_ui()

    def resume_music(self):
        mixer.music.unpause()
        # self.sound_playing = True
        self.paused = False
        self.set_music_ui()

    def set_music_ui(self):
        if self.sound_playing:
            stop_music_button = Button(ai_frame, text="Stop", height=2, width=26,
                                       command=self.stop_music).grid(row=2, column=1, sticky=N + S + W + E)
        else:
            play_music_button = Button(ai_frame, text="Play Again", height=2, width=26,
                                       command=self.play_music).grid(row=2, column=1, sticky=N + S + W + E)
        if self.paused:
            resume_music_button = Button(ai_frame, text='Resume', height=2, width=26,
                                         command=self.resume_music).grid(row=2, column=0, sticky=N + S + W + E)
        else:
            pause_music_button = Button(ai_frame, text='Pause', height=2, width=26,
                                        command=self.pause_music).grid(row=2, column=0, sticky=N + S + W + E)
