import numpy as np
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPool2D

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data(path='mnist.npz')

x_train = x_train / 255
x_test = x_test / 255

x_train = np.reshape(x_train, (x_train.shape[0], 28, 28, 1))
x_test = np.reshape(x_test, (x_test.shape[0], 28, 28, 1))

model = Sequential(
    [
        Conv2D(8, 3, input_shape=(28, 28, 1)),
        MaxPool2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(10, activation='softmax')
    ]
)

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=x_train, y=y_train, epochs=10)

model.evaluate(x_test, y_test)

model.save("model")
