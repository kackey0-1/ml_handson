# Model index
## Unsupervised Learning
### K-Means
### MeanShift
### Gaussian Mixture Model(=GMM)
### Variational Bayesian Gaussian Mixture(= VBGM)

### Hierarchical Clustering
Hierarchical Clustering creates clusters using a hierarchical tree. 
It may be effective on recommendation system but it is heavy with a lot of data.

## Supervised Learning
### Linear Model
- Simple Linear Model
- L1 Lasso Regression
  - linear model with penalties
- L2 Ridge Regression
  - [//]: # (TODO)
- Logistic Regression
  - Binary Logistic Regression
  - Multiclass Logistic Regression

### KNN(K-Nearest Neighbor)
- supervised ML algorithm for classification

### SVM(Support Vector Machine)
- supervised ML algorithm for classification
  1. K-NN distances are computed 
  2. These distances are not between data points, but with hyper-plane, that better divides different classifications

### XGBoost
  - Optimized Gradient Boosting algorithm through parallel processing tree-pruning, handling missing values and regularization to avoid over-fitting / bias
  - Evolution of version of Decision Trees. this has been widely used in fraud detection field(unsupervised learning). and has had many positive results.
### Deep Learning

#### Convolutional Neural Networks
- Used for image classification
- Used with 
  - Kernel Selection
    - filters or kernels are computations on a sub-matrix of pixels
    - We use multiple convolution filters or kernels that run over the image and compute a dot product
  - Stride
    - the amount of stride we choose affects the size of the feature extracted
  - Max Pooling Layer
    - Max pooling layer helps reduce the spatial size of the convolved features and also helps reduce over-fitting by providing an abstracted representation of them
- [//]: # (TODO Check which problem is suitable for)

#### Matrix Factorization
- Used for recommendation system
- Can be used with Collaborative Filtering

#### FeedForward Neural Networks
The classic example of neural networks. In fact, they were the first and most elementary type of artificial neural network.    

Feedforward Neural Networks are mainly used for supervised learning when data, mainly numerical, to be learned is neither time-series nor sequential(Such as NLP)

#### Recurrent Neural Network
Recurrent Neural Network is a class of artificial neural networks where connections between nodes form a directed graph along temporal sequence.

#### Transformers
Deep learning model that can give different importance to each part of the input data. this is used for NLP(Natural Language Processing and Computer Vision) area

#### GAN Generative Adversarial Learning
GAN is a special class of machine learning frameworks used for the automatic generation of facial images.
GAN can create new cha

#### Autoencoder and self-encoder
Neural Network aimed to transform and learn with a compressed representation of raw data.(Unsupervised Learning)

Autoencoder and self-encoder are useful when you need to reduce the number of variables under consideration for the model, therefore for dimentionality reduction.

#### Collaborative Filtering
Collaborative Filtering works the idea that a user may like same things of the people with similar profiles and preferences. So exploiting the choices of other users, the recommendation system makes a guess and can advise people on things not yet been rated by them.
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml33.png">

## Reinforcement Learning(RL)
RL provides a software agent that evaluates possible solutions through a progressive reward in repeated attempts.
it does not require labels. But it requires a lot of data and several trial and the possibility to evaluate the validity of each attempt.
- Q-Learning
- deep Q-network(DQN)
- deep deterministic policy gradient

[//]: # (TODO summarize other models evaluation)
# ML Evaluation 
- Classification model
  - Binary Classification
    - When there is an imbalance between true and false ratio, it is necessary to modify the classification threshold
    - https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall
      - Precision: Rate of correct positive identification
      - Recall: Rate of real positive correctly identified

## Cross-Validation
Cross-Validation involves running out modeling process on various subsets of data.
Obviously, Cross-Validation creates a computational load. Therefore, it can be prohibitive in very large datasets, but it is great when you have smalll datasets

<img scr="https://s3.amazonaws.com/media.whizlabs.com/learn/38.png">


