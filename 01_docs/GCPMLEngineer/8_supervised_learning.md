## Supervised Learning
### Linear Model
- Simple Linear Model
- L1 Lasso Regression
  - linear model with penalties
- L2 Ridge Regression
  - [//]: # (TODO)
- Logistic Regression
  - Binary Logistic Regression
    - Logistic Regression, you have to train the model and figure out the parameters of specific function that best fit the data before the inference.
  - Multiclass Logistic Regression

### SVM(Support Vector Machine)
- supervised ML algorithm for classification
  1. K-NN distances are computed 
  2. These distances are not between data points, but with hyper-plane, that better divides different classifications

### Lazy Learning (Oposite of Eager Learning)
Lazy Learning means that the algorithm only stores the data of the training part without learning a function. The stored data will then be used for the evaluation of new query point.

#### K-Nearest Neighbors
KNN is one of Lazy Learing algorithm for both classification and regression problems.
You begin with data that is already classified. A new example will be set by looking at the nearest classified points. Number k is the most important hyperparameter.

#### Naive Bayes
Naive Bayes is one of Lazy Learning algorithm for classification problem.
The features have to be independent. It requires a small amount of training data.

#### KNN(K-Nearest Neighbors)
- supervised ML algorithm for classification and regression


### Ensumble Learning 
Ensemble Learning is performed by multiple learning algorithm working together for higher predictive performance.

#### XGBoost
- Optimized Gradient Boosting algorithm through parallel processing tree-pruning, handling missing values and regularization to avoid over-fitting / bias
- Evolution of version of Decision Trees. this has been widely used in fraud detection field(unsupervised learning). and has had many positive results.



### Deep Learning
#### Simple Nueral Network
Neural Network, you have to train the model and figure out the parameters of a specific function that best fit the data before the inference.

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

---