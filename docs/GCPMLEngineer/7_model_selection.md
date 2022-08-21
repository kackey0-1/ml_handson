# How we should select ML model for each case

## The problem is that you don't know the difference between parametric and nunparametric algorithms. So you looked for it.
### Non-Parametric
Non-Parametric method refers to a method that does not assume any distribution with any function with parameters.

- K-Nearest Neighbors
  - K-Nearest Neighbors is a simple supervised algorithm both classification and regression problems.
  - You begin with data that is already classified. A new example will be set by looking at the k nearest classified points. Number k is the most important hyperparameter.
- Decision Tree
  - a Decision Tree has a series of tests inside a flowchart-like structure. So no methematical functions to solve.

### Parametric
You have to figure out the parameters of a specific function that best fit the data.
- Simple Neural Networks
- Logistic Regression
  

## Your manager told you that you should try ensemble methods intrigued, you are documented. Which of the following are ensemble-type algorithms.

### Ensumble Learning 
Ensemble Learning is performed by multiple learning algorithm working together for higher predictive performance.

### Random Forests 
Random Forests are made that multiple decision trees, randome sampling, a subset of variables and optimzation techniques at each step (Voting the best model)

AdoBoost is built with multiple decision trees, too, with the following differences.
1. it creates stumps, that is, trees with only one node and two leaves.
2. Stumps with less error with
3. Ordering is built in such a way as to reduce errors
 
### Gradient Boost
Gradient Boost is built with multiple decision trees, too, with following differences from AdoBoost.

1. Trees instead stumps
2. It uses a loss function to minimize errors
3. Trees are selected to predict the difference from actual values

### XGBoost
XGBoost is currently very popular. It is similar to Gradient Boost with the following differences
- Leaf node proning, that is regularization in order to keep the best ones for generalization.
- Newton Boosting instead of gradient descent, so math-based and faster
- Correlation between trees reduction with an additional randomization parameter
- Optimized algorithm for tree penalization


Note: Deep&Cross Network are a new kind of Neural Networks. Decision Trees are flowchart like with a series of tests on the nodes. So both of them use one kind of method


