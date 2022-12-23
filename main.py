import numpy as np
import scipy

def pprint(n: int):
    for _ in range(n):
        print("#", end='')


if __name__ == '__main__':
    # pprint(10)

    nums = np.array([[0, 1], [2, 3]])
    print(scipy.cov(nums))




