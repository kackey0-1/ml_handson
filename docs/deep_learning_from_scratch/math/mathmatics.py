import numpy as np


if __name__ == '__main__':
    # 行列の作成
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = np.array([[5], [6]])

    print(a.shape)
    print(b.shape)
    print(c.shape)
    # 行列の積
    print(np.dot(a, b))
    # 行列の積
    print(np.dot(a, c))
