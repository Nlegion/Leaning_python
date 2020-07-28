import numpy as np


def sigmoid(x):  # функция активации
    return 1 / (1 + np.exp(-x))


def training(tr_inputs, tr_outputs, s_weights): #функция обучения
    outputs = 0
    for i in range(20000):# метод обратного распространения
        input_layer = tr_inputs
        outputs = sigmoid(np.dot(input_layer, s_weights))
        err = tr_outputs - outputs
        adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
        s_weights += adjustments
    return s_weights


training_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1
synaptic_weights = training(training_inputs, training_outputs, synaptic_weights)
new_inputs = np.array([1, 1, 0])
output = sigmoid(np.dot(new_inputs, synaptic_weights))
print(output)
