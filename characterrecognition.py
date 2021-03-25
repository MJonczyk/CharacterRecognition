from tkinter import *
from tkinter import ttk
from sketchpad import Sketchpad
import numpy as np


class CharacterRecognition:
    def __init__(self, root, model):
        self.root = root
        root.title('Character Recognition')

        self.model = model

        self.mainframe = ttk.Frame(root, padding="0 0 0 10")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.sketchpad_frame = ttk.Frame(self.mainframe, borderwidth=2, relief='sunken')
        self.sketchpad_frame.grid(column=0, row=0, columnspan=2)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.label_text = StringVar()
        self.label = ttk.Label(self.mainframe, text='', width=12)
        self.label.grid(column=0, row=1)

        self.sketchpad = Sketchpad(self.sketchpad_frame, width=280, height=280, background='white')
        self.sketchpad.grid(column=0, row=0, sticky=(N, W))
        self.sketchpad.bind("<ButtonRelease-1>",
                            lambda e: self.label.configure(text='Recognized ' + str(
                                np.argmax(
                                    self.model.predict(
                                        np.reshape(self.sketchpad.pixels,
                                                   (1, 28, 28, 1)))))))

        self.button = ttk.Button(self.mainframe, text='Clear', command=self.clear)
        self.button.grid(column=1, row=1, padx=10, pady=10)

    def clear(self):
        self.label.configure(text='')
        self.sketchpad.delete('all')
        self.sketchpad.clear()
