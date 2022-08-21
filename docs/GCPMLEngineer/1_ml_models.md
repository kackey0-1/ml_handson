# Model index
## Unsupervised Learning
### K-Means
### MeanShift
### Gaussian Mixture Model(=GMM)
### Variational Bayesian Gaussian Mixture(= VBGM)

### Hierarchical Clustering
Hierarchical Clustering creates clusters using a hierarchical tree. 
It may be effective on recommendation system but it is heavy with a lot of data.

---

## Reinforcement Learning(RL)
RL provides a software agent that evaluates possible solutions through a progressive reward in repeated attempts.
it does not require labels. But it requires a lot of data and several trial and the possibility to evaluate the validity of each attempt.
- Q-Learning
- deep Q-network(DQN)
- deep deterministic policy gradient

[//]: # (TODO summarize other models evaluation)

---

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


