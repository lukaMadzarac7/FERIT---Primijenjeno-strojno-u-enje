import numpy as np
from tensorflow import keras
from keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = keras.Sequential()
model.add(layers.Input(shape=(28,28,1), name = "ulaz"))
model.add(layers.Conv2D(32, kernel_size = (3,3), padding='same', activation= 'relu'))
model.add(layers.MaxPool2D(pool_size=(2,2), strides = (2,2)))
model.add(layers.Conv2D(64, kernel_size = (3,3), padding='same', activation= 'relu'))
model.add(layers.MaxPool2D(pool_size=(2,2), strides = (2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(200, activation = 'relu'))
model.add(layers.Dropout(rate=0.5))
model.add(layers.Dense(50, activation = 'relu'))
model.add(layers.Dense(10, activation = 'softmax', name = "izlaz"))
model.summary()


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics='accuracy')

# TODO: provedi ucenje mreze
model.fit(x_train_s, y_train_s, epochs=5, batch_size=32)



# TODO: Prikazi test accuracy i matricu zabune
score = model.evaluate(x_test_s, y_test_s, verbose=0)
print("Text loss: ", score[0])
print("Test accuracy: ", score[1])


# TODO: spremi model

model.save("mymodel")


