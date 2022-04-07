# Neural Network
## Activation関数

閾値を境にして出力が切り替わる関数
ニューラルネットワークでは、活性化関数を用いて信号の変換を行い、その変換された信号が次のニューロンに送られる


## Sigmoid Function
- 非線形関数

$$ h(x) = \frac{1}{1 + e^{-x}} $$


## Relu(Rectified Linear Unit) Function
- 線形関数
- 近年では主要に利用されている

$$
h(x) =
\begin{cases}
  x \quad x \geqq 0 \\
  0 \quad x < 0 \\
\end{cases} 
$$

## Softmax Function
- softmax function
  - Used for Classification Model
  - Feature of Softmax Function
    - 総和は`1`になる
    - ニューラルネットワークのクラス分類では、出力が最も大きいものを出力結果とする(= np.max(a))
    - 推論フェーズでは、出力層ではソフトマックス関数を利用しないのが一般的(出力結果に対してソフトマックス関数を利用しても、大小は変わらないため)
    - 学習フェーズではもちろん利用

### Softmax function that might overflow
$$ y_k = \frac{\exp(a_k)}{\sum_{i=0}^{n}\exp(a_i)} $$

### Softmax function that prevent from overflow
$$ y_k = \frac{\exp(a_k+C')}{\sum_{i=0}^{n}\exp(a_i+C')} $$
