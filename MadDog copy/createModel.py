import os
import tensorflow as tf
import numpy as np

currentDirectory = os.getcwd()
name = "Giri"

with open(f'{currentDirectory}/data/{name}_data/x_train.txt', 'r') as file:
    x_train_str = file.readlines()

print("1")

with open(f'{currentDirectory}/data/{name}_data/y_train.txt', 'r') as file:
    y_train_str = file.readlines()

print("2")

x_train = []
for line in x_train_str:
    cur = line.split()
    for i in range(len(cur)):
        cur[i] = int(cur[i])
    x_train.append(np.array(cur))

y_train = []
for line in y_train_str:
    cur = []
    for simbol in line:
        if simbol == '\n':
            continue
        cur.append(int(simbol))
    add = ((cur[0] - 1) * 8 + cur[1] - 1) * 64 + ((cur[2] - 1) * 8 + cur[3] - 1)
    y_train.append(add)

print("a")

#x_train = tf.keras.utils.normalize(x_train, axis=2)

x_train = np.array(x_train)
y_train = np.array(y_train)

print(f'x_train shape => {x_train.shape}')
print(f'y_train shape => {y_train.shape}')

print("b")

#print(x_train)
#print(y_train)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(4096, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(1024, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(526, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(64 * 64, activation = tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics='accuracy')

model.fit(x_train, y_train, epochs=15)
model.save(f'{name}_model.model')