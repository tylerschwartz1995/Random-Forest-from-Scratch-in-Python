# Random-Forest-from-Scratch-in-Python
Programming random forest from scratch using Python.

# Summary
The goal of this project is to reproduce the Random Forest algorithm from scratch and with the lowest usage of external libraries.

We will propose to the user as much as flexibility as possible:
- Categorical vs Regression
- Categorical feature transformation (One-Hot-Encoding, Target-Encoding, Frequency-Encoding)
- Possibility to handle missing values with different sort of imputation
- Parallelisation of the CART tree building
- etc.

Building the random forest from scratch means:
- Building the CART tree algorithm
- Bagging of the data
- Random sampling of the feature

Based on our reading on CATBoost, XGBoost and LightGBM, we will introduce ideas to faster and improve our algorithm:
- Depth Search vs Breath Search
- Binning of the feature
- Categorical to Continuous strategies
- Cross validation between split search and node evaluation
- etc.

...

# Members
In alphabetique order:
- Lin Lin
- Maxime Jousset
- Tyler Schwartz
