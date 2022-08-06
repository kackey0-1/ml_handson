import numpy as np
import pickle
from deep_learning_from_scratch.dataset.mnist import load_mnist
from deep_learning_from_scratch.common.activation.activation_functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    """
    Create 3 layered neural network
    :return:
    """
    with open('sample/sample_weight.pkl', 'rb') as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # print(x.shape)
    # print(W1.shape)
    # print(W2.shape)
    # print(W3.shape)

    z1 = np.dot(x, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)
    z3 = np.dot(a2, W3) + b3
    a3 = sigmoid(z3)
    y = softmax(a3)

    return y


def main_without_batch():
    x, t = get_data()
    network = init_network()
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)

        if p == t[i]:
            accuracy_cnt += 1
    print(f'Accuracy: {str(float(accuracy_cnt) / len(x))}')


def main_with_batch():
    x, t = get_data()
    network = init_network()

    batch_size = 100  # batch size(一気に処理する数)
    accuracy_cnt = 0
    for i in range(0, len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)
        print(p)
        print(t[i:i+batch_size])
        accuracy_cnt += np.sum(p == t[i:i+batch_size])
    print(f'Accuracy: {str(float(accuracy_cnt) / len(x))}')


if __name__ == '__main__':
    print('##############################################')
    main_without_batch()
    print('##############################################')
    main_with_batch()

