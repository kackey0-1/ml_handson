# Neural Network
## Activation関数

閾値を境にして出力が切り替わる関数
ニューラルネットワークでは、活性化関数を用いて信号の変換を行い、その変換された信号が次のニューロンに送られる


## Sigmoid Function
$$ h(x) = \frac{1}{1 + e^{-x}} $$

- 非線形関数

## Relu(Rectified Linear Unit) Function
- 近年では主要に利用されている

$$
h(x) =
\begin{cases}
  x \quad x \geqq 0 \\
  0 \quad x < 0 \\
\end{cases} 
$$
