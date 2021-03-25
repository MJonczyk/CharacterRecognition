from tkinter import *
import numpy as np


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.pixels = np.zeros(shape=(28, 28))
        self.bind("<B1-Motion>", self.draw)
        self.bind("<Button-1>", self.draw)

    def draw(self, event):
        self.create_oval((event.x - 10, event.y - 10, event.x + 10, event.y + 10), fill='black')
        x = event.x // 10
        y = event.y // 10

        if x <= 0:
            x = 0
        elif x >= 28:
            x = 27

        if y <= 0:
            y = 0
        elif y >= 28:
            y = 27

        self.pixels[y][x] = 1

        if y > 0 and x > 0:
            if self.pixels[y - 1][x - 1] == 0:
                self.pixels[y - 1][x - 1] = 0.5
        if y > 0 and x < 27:
            if self.pixels[y - 1][x + 1] == 0:
                self.pixels[y - 1][x + 1] = 0.5
        if y < 27 and x > 0:
            if self.pixels[y + 1][x - 1] == 0:
                self.pixels[y + 1][x - 1] = 0.5
        if y < 27 and x < 27:
            if self.pixels[y + 1][x + 1] == 0:
                self.pixels[y + 1][x + 1] = 0.5
        if y > 0:
            if self.pixels[y - 1][x] == 0:
                self.pixels[y - 1][x] = 0.5
        if x > 0:
            if self.pixels[y][x - 1] == 0:
                self.pixels[y][x - 1] = 0.5
        if y < 27:
            if self.pixels[y + 1][x] == 0:
                self.pixels[y + 1][x] = 0.5
        if x < 27:
            if self.pixels[y][x - 1] == 0:
                self.pixels[y][x + 1] = 0.5

    def clear(self):
        self.pixels = np.zeros(shape=(28, 28))
