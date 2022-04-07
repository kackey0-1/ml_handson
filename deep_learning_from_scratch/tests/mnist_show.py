import sys
import os
import numpy as np
from deep_learning_from_scratch.dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


if __name__ == '__main__':
    (x_train, x_test), (t_train, t_test) = load_mnist(flatten=True, normalize=False)
    img = x_train[0]
    label = t_train[0]
    print(label)
    print(img.shape)
    print(img.shape)
    img = img.reshape(28, 28)
    label = label.reshape(28, 28)
    img_show(label)
    img_show(img)
