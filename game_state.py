from tkinter import *
from tkinter import messagebox
import threading
from static_ui import raise_frame, start_frame, face_rec_frame, ai_frame, window
from emotion_classifier import emotion_recognition, action


class GameState:
    def __init__(self, x, e, dui, mp, em):
        self.x = x
        self.e = e
        self.dui = dui
        self.mp = mp
        self.em = em

    def start(self, try_again=False):
        if try_again:
            self.reset_frame()
        raise_frame(face_rec_frame)
        self.e.clear()
        self.x.start()

    def reset_thread(self):
        self.x.join()
        self.e.set()
        self.x = threading.Thread(target=emotion_recognition, args=(self.e, self.dui))

    def start_menu(self):
        self.reset_thread()
        raise_frame(start_frame)

    def try_again(self):
        if self.mp.sound_playing:
            self.mp.stop_music()
        self.start(True)

    def quit_app(self):
        if messagebox.askyesno(title='Quit', message='Do You Really Want to Quit?'):
            window.destroy()
        else:
            pass

    def go_back(self):
        if messagebox.askyesno(title='Go Back To Main Menu', message='Do You Want To Go Back To The Main Menu?'):
            self.start_menu()
        else:
            pass

    def check_user_emotion(self):
        self.reset_thread()
        yes_text, reaction_text, emotion = self.react_to_user()
        reaction_option_text = Label(face_rec_frame, text=reaction_text, anchor=CENTER, background="black",
                                     font=("Helvetica", 14), fg="white", width=100,
                                     height=2).grid(row=2, column=0, columnspan=2, sticky=N + S + W + E)
        yes_button = Button(face_rec_frame, text=yes_text, height=2, width=26,
                            command=lambda: self.em.map_emotion(emotion)).grid(row=3, column=0, sticky=N + S + W + E)
        no_button = Button(face_rec_frame, text="Try Again!", height=2, width=26,
                           command=lambda: self.start(try_again=True)).grid(row=3, column=1, sticky=N + S + W + E)

    def react_to_user(self):
        emotion_check = action()
        print(emotion_check)
        self.dui.frame_stream(emotion_check + 'Reaction')
        print('You\'re feeling: ', emotion_check)
        return self.reaction_options(emotion_check)

    def reaction_options(self, emotion):
        if emotion == 'Happy':
            return 'Let\'s Dance!!', 'We Should Celebrate!', 'Happy'
        elif emotion == 'Sad':
            return 'Yes, Please! :(', 'Can I Tell You A Joke?', 'Sad'
        elif emotion == 'Angry':
            return 'Help me relax!', 'Should We Count Down From 10?', 'Angry'
        elif emotion == 'Surprise':
            return 'Fun fact please!', 'You Want To Hear Something Crazy?!', 'Surprise'

    def reset_frame(self):
        check_button = Button(face_rec_frame, text="Check My Emotion", height=2, width=26,
                              command=self.check_user_emotion).grid(row=2, column=0, columnspan=2, sticky=N + S + W + E)
        exit_button = Button(face_rec_frame, text="End Emotion Recognition", height=2, width=26,
                             command=self.go_back).grid(row=3, column=0, columnspan=2, sticky=N + S + W + E)
        try_again_button = Button(ai_frame, text='Try Again', height=2, width=26,
                                  command=self.try_again).grid(row=4, column=0, columnspan=2, sticky=N + S + W + E)
