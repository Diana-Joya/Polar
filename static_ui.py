from tkinter import *
from PIL import Image, ImageTk

# -------------------- GUI --------------------
window = Tk()
window.title("Emotion Recognition")
window.configure(background='black')

# ------------------ Graphics Windows ------------------
# Start Frame
start_frame = Frame(window, width=600, height=600)
start_frame.grid(row=0, column=0, sticky=N+S+W+E)
start_frame.grid_rowconfigure(0, weight=1)
start_frame.grid_rowconfigure(1, weight=1)
start_frame.grid_columnconfigure(0, weight=1)

# Face Recognition Frame
face_rec_frame = Frame(window, width=800, height=600)
face_rec_frame.grid(row=0, column=0, columnspan=2, sticky=N+S+W+E)
face_rec_frame.grid_rowconfigure(0, weight=1)
face_rec_frame.grid_rowconfigure(1, weight=1)
face_rec_frame.grid_rowconfigure(2, weight=1)
face_rec_frame.grid_columnconfigure(0, weight=1)
face_rec_frame.grid_columnconfigure(1, weight=1)

# AI Frame
ai_frame = Frame(window, width=800, height=600)
ai_frame.grid(row=0, column=0, sticky=N+S+W+E)
ai_frame.grid_rowconfigure(0, weight=1)
ai_frame.grid_rowconfigure(1, weight=1)
ai_frame.grid_rowconfigure(2, weight=1)
ai_frame.grid_columnconfigure(0, weight=1)


def raise_frame(frame):
    frame.tkraise()


# ------------------ Start Window -------------------
main_title_text = Label(start_frame, text="Welcome to my application", anchor=CENTER, background="LightSkyBlue2",
                        font=("Helvetica", 14), fg="SlateBlue2", width=100, height=2).grid(row=0, column=0, sticky=N+S+W+E)
startScreen = 'polar/screens/startScreen.png'
img = ImageTk.PhotoImage(Image.open(startScreen))
startImg = Label(start_frame)
startImg.grid(row=1, column=0, sticky=N+S+W+E)
startImg.imgtk = img
startImg.configure(width=450, height=500, image=startImg.imgtk)


# ------------------- F.R. Window -------------------
fr_title_text = Label(face_rec_frame, text="Can I Guess How You Are Feeling?", anchor=CENTER,
                      background="black", font=("Helvetica", 14),
                      fg="white", height=2).grid(row=0, column=0, columnspan=2, sticky=N+S+W+E)


# ------------------ AI Window -------------------
ai_title_text = Label(ai_frame, text="AI Window", anchor=CENTER,
                      background="black", font=("Helvetica", 14),
                      fg="white", width=100, height=2).grid(row=0, column=0, columnspan=2, sticky=N+S+W+E)
reset_emotion_button = Button(ai_frame, text="Restart Emotion Recognition", height=2, width=26,
                              command=lambda: raise_frame(face_rec_frame)).grid(row=3, column=1, sticky=N+S+W+E)

display1 = Label(face_rec_frame)
display1.grid(row=1, column=1, columnspan=1, sticky=N+S+W+E)
display2 = Label(face_rec_frame)
display2.grid(row=1, column=0, columnspan=1, sticky=N+S+W+E)
ai_display = Label(ai_frame)
ai_display.grid(row=1, column=0, columnspan=2, sticky=N + S + W + E)