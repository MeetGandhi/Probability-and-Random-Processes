The folder contains two implementations of PCA on iris dataset as well as digits dataset.

For PCA implementation on iris dataset run testupgraded.py:
https://archive.ics.uci.edu/ml/datasets/iris

For PCA implementation on digits dataset run testdig.py: http://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits

1)

As you run testupgraded.py which is PCA implementation on iris dataset you will be presented with plots of Percentage Explained Variance VS (Principal Component-1) and Cumulative Explained variance VS (Principal Component-1).

The above two plots will help the user to determine upto which principal components the variance in the data is significant and hence the user can efficiently determine the number of reduced dimensions.

As there are only 4 principal components in iris data:

If you enter 1 you will be presented with a 1D scatter plot of the principal component with the highest variance.

If you enter 2 you will be presented with a 2D scatter plot of the principal components with the highest and second highest variances.

If you enter 3 you will be presented with a 2D scatter plot of the principal components with the highest, second highest and third highest variances.

For 4, as there are will be not representation available though we can do it, the representation won't add any value to the task we are intended to perform i.e. PCA implementation: https://stackoverflow.com/questions/31806254/plotting-4d-data

2)

As you run testdig.py which is PCA implementation on digits dataset you will be presented with plots of Percentage Explained Variance VS (Principal Component-1) and Cumulative Explained variance VS (Principal Component-1).

The above two plots will help the user to determine upto which principal components the variance in the data is significant and hence the user can efficiently determine the number of reduced dimensions.

If you enter 1 you will be presented with a 1D scatter plot of the principal component with the highest variance.

If you enter 2 you will be presented with a 2D scatter plot of the principal components with the highest and second highest variances.

If you enter 3 you will be presented with a 2D scatter plot of the principal components with the highest, second highest and third highest variances.

For rest, the scatter plots are not programmed.
