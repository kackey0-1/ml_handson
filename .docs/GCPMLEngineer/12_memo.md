# About Baysian Optimization
<!-- TODO -->

# About SGD
- Stochastic Gradient Descent
  - Stochastic Gradient Descent(SGD)
    - SGD is the idea to the extreme-it uses only a single example(a batch size of 1) per iteration, which gitves enough iterations
- Mini-Batch stochastic gradient descent
  - mini-batch SGD is a compromise between full-batch iteration and SGD
  - a mini batch is typically between 10 and 1000 examples

To ensure a good representative sample, the algorithm scoops up another random small batch (or batch of one) on every iteration

# About Feature Cross
- Crossing real valued features is not good idea
  - Crossing the real value of latitude with roomsPerPerson enables a 10% change in one feature to be equivalent to a 10% change in the other feature
- Crossing binned latitude with binned longitude enables the model to learn city-specific effects of roomsPerPerson
  - Binning prevents a change in latitude producing the same result as a change in longitude
  - Depending on the granularity of the bins, this feature cross could learn city-specific or neighborhood-specific or even block-specific effects.

# About L2 Regularization
- L2 regularization encourages weighs to be near 0.0, but not exactly 0.0
- L2 regularization may cause the model to learn a moderate weight for some non-informative features
  - Surprisingly this can happen when a non-informative feature happens to be correlated with the label
  - in this case, the model incorrectly gives such non-informative features some of the credit that should have gone to informative features
- L2 Reguration will force the features towards roughly equivalent weights that are approximately half of what they would have been had only one of the two features been in the model
