import numpy as np


class Perceptron:
    """
    Perceptron is an algorythem which have input and output.
    If input is given, perceptron returns output.
    Perceptron takes **weight** and **bias** as parameters.
    - Pros
      - 複雑な関数であっても層を重ねると非線形のような表現可能
    - Cons
      - 重ねを設定する作業は全て手作業になる
    """

    def AND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        tmp = np.sum(w * x) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7
        tmp = np.sum(w * x) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def OR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.2
        tmp = np.sum(w * x) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def XOR(self, x1, x2):
        s1 = self.NAND(x1, x2)
        s2 = self.OR(x1, x2)
        y = self.AND(s1, s2)
        return y


if __name__ == '__main__':
    perceptron = Perceptron()
    print("###############################")
    print(perceptron.AND(0, 0))
    print(perceptron.AND(0, 1))
    print(perceptron.AND(1, 0))
    print(perceptron.AND(1, 1))
    print("###############################")
    print(perceptron.NAND(0, 0))
    print(perceptron.NAND(0, 1))
    print(perceptron.NAND(1, 0))
    print(perceptron.NAND(1, 1))
    print("###############################")
    print(perceptron.OR(0, 0))
    print(perceptron.OR(0, 1))
    print(perceptron.OR(1, 0))
    print(perceptron.OR(1, 1))
    print("###############################")
    print(perceptron.XOR(0, 0))
    print(perceptron.XOR(0, 1))
    print(perceptron.XOR(1, 0))
    print(perceptron.XOR(1, 1))
