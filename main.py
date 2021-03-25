from tkinter import *
from characterrecognition import CharacterRecognition
from tensorflow import keras

if __name__ == '__main__':
    model = keras.models.load_model("model")

    root = Tk()
    cr = CharacterRecognition(root, model)
    root.mainloop()
