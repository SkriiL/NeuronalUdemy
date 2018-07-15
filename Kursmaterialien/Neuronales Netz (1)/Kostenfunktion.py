import gzip
import numpy as np
from scipy.special import expit
from sklearn.preprocessing import OneHotEncoder
import pickle


def open_images(filename):
    with gzip.open(filename, "rb") as file:
        data = file.read()
        return np.frombuffer(data, dtype=np.uint8, offset=16)\
            .reshape(-1, 28, 28)\
            .astype(np.float32)


def open_labels(filename):
    with gzip.open(filename, "rb") as file:
        data = file.read()
        return np.frombuffer(data, dtype=np.uint8, offset=8)


X_test = open_images("../mnist/t10k-images-idx3-ubyte.gz").reshape(-1, 784)
y_test = open_labels("../mnist/t10k-labels-idx1-ubyte.gz")

class NeuralNetwork(object):
    def __init__(self):
        with open("w0.p", "rb") as file:
            self.w0 = pickle.load(file)
        with open("w1.p", "rb") as file:
            self.w1 = pickle.load(file)


    def activation(self, x):
        return expit(x)

    def predict(self, X):
        a0 = self.activation(self.w0 @ X.T)
        pred = self.activation(self.w1 @ a0)
        return pred

    def cost(self, pred, y):
        # SUM((y - pred)^2)
        s = (1 / 2) * (y.T - pred) ** 2
        return np.mean(np.sum(s, axis=0))

model = NeuralNetwork()
# print(model.w0.shape)
# print(model.w1.shape)

# Kostenfunktion
oh = OneHotEncoder()
y_test_oh = oh.fit_transform(y_test.reshape(-1, 1)).toarray()
print(model.cost(model.predict(X_test / 255.), y_test_oh))

y_test_pred = model.predict(X_test / 255.)
y_test_pred = np.argmax(y_test_pred, axis=0)
print(np.mean(y_test_pred == y_test))