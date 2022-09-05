## Neural Network実装
- A: Activation
- X: Input
- W: weight
- B: bias

![](https://camo.qiitausercontent.com/6cc0a9c152f4a826725c5574a087de23ce6d6dea/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3230393730352f64373830626534612d363865342d666532302d636434652d6230346431646166396663372e706e67)

### 行列の積 by Numpy
$$
\begin{pmatrix}
1&2\\
3&4
\end{pmatrix}
\begin{pmatrix}
5&6\\
7&8
\end{pmatrix}
=
\begin{pmatrix}
19&22\\
43&50
\end{pmatrix}
$$

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([[5], [6]])
# 行列の積
print(a.shape)
print(b.shape)
print(c.shape)
print(np.dot(a, b))
print(np.dot(a, c))
```

### 3層ニューラルネットワーク
以下のような数式で1層目を表すことができる。
$$ a_{1}^{(1)} = w_{11}^{(1)}x_{1} + w_{12}^{(1)}x_{2} + b_{1}^{(1)}  $$
これを行列の席を用いると、第1層目の重み付き和は次の式で表すことができる

$$ A^{(1)} = XW^{(1)} + B^{(1)} $$

$$ 
A^{(1)} = \begin{pmatrix} a_{1}^{(1)} &a_{2}^{(1)} &a_{3}^{(1)} \end{pmatrix},
X = \begin{pmatrix} x_{1} &x_{2} \end{pmatrix}, 
B^{(1)} = \begin{pmatrix} b_{1}^{(1)} &b_{2}^{(1)} &b_{3}^{(1)} \end{pmatrix},
W^{(1)} = \begin
{pmatrix} w_{11}^{(1)} &w_{21}^{(2)} &w_{31}^{(1)} \\
w_{12}^{(1)} &w_{22}^{(2)} &w_{32}^{(1)} 
\end {pmatrix}
 $$


