import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    return

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


if __name__ == '__main__':
    activations = [sigmoid, relu]
    x = np.array([_ for _ in range(-7, 7)])

    for func in activations:
        print('######### {} #########'.format(func.__name__))
        fig, ax = plt.subplots(figsize=(4, 4))
        print(x.shape)
        print(func(x).shape)
        sns.lineplot(x, func(x))
        fig.suptitle(func.__name__)
    plt.show()
