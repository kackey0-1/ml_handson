import seaborn as sns
import numpy as np


x = np.array([ _ for _ in range(-7, 7)])
y = 1 / (1 + np.exp(-x))
print(x.shape)
print(y.shape)
sns.lineplot(x, y)