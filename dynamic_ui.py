import cv2
from tkinter import *
from PIL import Image, ImageTk
import random
from static_ui import ai_frame, display1, display2


class DynamicUI:
    def __init__(self):
        self.current = "Neutral"

    def face_stream(self, img1):
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGBA)
        imgtk1 = ImageTk.PhotoImage(image=Image.fromarray(img1))
        display1.imgtk = imgtk1
        display1.configure(width=600, height=400, image=imgtk1)

    def frame_stream(self, label):
        path = "polar/emotions/" + label + ".png"
        img = ImageTk.PhotoImage(Image.open(path))
        display2.imgtk = img
        display2.configure(width=500, height=450, image=display2.imgtk, bg="white")

    def ai_frame_stream(self, label, action):
        self.current = label
        ai_display = Label(ai_frame)
        if label == 'Sad' or label == 'Surprise':
            ai_display.grid(row=1, column=1, sticky=N + S + W + E)
            resize = (400, 400)
        elif label == 'Angry':
            ai_display.configure(bg="black")
            ai_display.grid(row=1, column=0, columnspan=2, sticky=N + S + W + E)
            resize = (800, 460)
        else:
            ai_display.grid(row=1, column=0, columnspan=2, sticky=N + S + W + E)
            resize = (440, 450)
        path = "polar/reactions/" + label + "/" + action + ".png"
        img = Image.open(path)
        img = img.resize(resize, Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(img)
        ai_display.imgtk = imgtk
        ai_display.configure(width=450, height=450, image=ai_display.imgtk)

    def set_emotion_title(self, text):
        ai_title_text = Label(ai_frame, text=text, anchor=CENTER,
                              background="LightSkyBlue2", font=("Helvetica", 14),
                              fg="SlateBlue2", width=100, height=2).grid(row=0, column=0, columnspan=2, sticky=N + S + W + E)

    def set_speech_bubble(self, text):
        colors = ['Blue Bubble', 'Green Bubble', "Purple Bubble", "Light Blue Bubble"]
        color = random.choice(colors)
        path = "polar/speech bubbles/" + color + ".png"
        background_img = Image.open(path)
        background_img = background_img.resize((470, 450), Image.ANTIALIAS)
        bktk = ImageTk.PhotoImage(background_img)
        speech_display = Label(ai_frame)
        speech_display.image = bktk
        speech_display.grid(row=1, column=0, sticky=N + S + W + E)
        speech_display.configure(width=450, height=450, image=speech_display.image, text=text, wraplength=250,
                                 font=("Helvetica", 16), justify=CENTER, compound=CENTER)
