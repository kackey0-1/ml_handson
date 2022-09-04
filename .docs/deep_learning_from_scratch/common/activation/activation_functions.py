import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def identity_function(x):
    return x


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def overflow_softmax(x):
    """
    softmax activation which will overflow
    :param x:
    :return:
    """
    exp_x = np.exp(x)
    sum_exp_x = np.exp(exp_x)
    return exp_x / sum_exp_x


def softmax(x):
    """
    softmax activation with prevention of overflow
    :param x:
    :return:
    """
    # use C to avoid overflow
    C = np.max(x)
    exp_x = np.exp(x - C)
    sum_exp_x = np.exp(exp_x)
    return exp_x / sum_exp_x


if __name__ == '__main__':
    activations = [sigmoid, relu, overflow_softmax, softmax]
    x = np.array([_ for _ in range(-7, 7)])

    for func in activations:
        print('######### {} #########'.format(func.__name__))
        fig, ax = plt.subplots(figsize=(4, 4))
        y = func(x)
        print(x.shape)
        print(y.shape)
        print(y)
        sns.lineplot(x, y)
        fig.suptitle(func.__name__)
    plt.show()

    print('######### {} #########'.format(overflow_softmax.__name__))
    a = np.array([1010, 1000, 900])
    print(overflow_softmax(a))
    print('######### {} #########'.format(softmax.__name__))
    print(softmax(a))
