import cv2
from tkinter import *
from PIL import Image, ImageTk
from static_ui import ai_frame, ai_display, display1, display2


class DynamicUI:
    def __init__(self):
        pass

    def face_stream(self, img1):
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGBA)
        imgtk1 = ImageTk.PhotoImage(image=Image.fromarray(img1))
        display1.imgtk = imgtk1
        display1.configure(width=600, height=400, image=imgtk1)

    def frame_stream(self, label):
        path = "polar/emotions/" + label + ".png"
        # in Face Rec Frame
        img = ImageTk.PhotoImage(Image.open(path))
        display2.imgtk = img
        display2.configure(width=450, height=400, image=display2.imgtk)
        # in AI Frame
        ai_display.imgtk = img
        ai_display.configure(width=450, height=400, image=ai_display.imgtk)

    def set_emotion_title(self, text):
        ai_title_text = Label(ai_frame, text=text, anchor=CENTER,
                              background="black", font=("Helvetica", 14),
                              fg="white", width=100, height=2).grid(row=0, column=0, columnspan=2, sticky=N + S + W + E)
