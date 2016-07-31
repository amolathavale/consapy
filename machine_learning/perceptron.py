import numpy as np
import pandas as pd
import matplotlib.pyplot as plotter
from matplotlib.colors import ListedColormap 

class Perceptron (object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        print('Final Weights\n')
        print([i for i in self.w_])
        print('Final Errors\n')
        print([i for i in self.errors_])
        return self

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

# Visualize feature-wise smaple distribution
def datavis(X, y):
    plotter.scatter(X[:50,0], X[:50,1], color='red', marker='o', label='setosa')
    plotter.scatter(X[50:100,0], X[50:100,1], color='blue', marker='x', label='versicolor')
    plotter.xlabel('sepal length')
    plotter.ylabel('petal length')
    plotter.legend(loc='upper left')
    plotter.show()

""" Train the algorithm where X is the inputs and Y is the output """
def plot_epochs(X, y):
    plotter.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plotter.xlabel('Epochs')
    plotter.ylabel('Number of misclassifications')
    plotter.show()

"""--------Perceptron Client ------------- """

# Build dataset

# Plot the decision regions showing distribution in class
def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers=('s', 'x', 'o', '^', 'v')
    colors=('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap=ListedColormap(colors[:len(np.unique(y))])
# plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                         np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plotter.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plotter.xlim(xx1.min(), xx1.max())
    plotter.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plotter.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

# =========== Client code ============
df = pd.read_csv('~/consapy/datasets/iris.data', header=None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1) # Digitize Output
X = df.iloc[0:100, [0,2]].values # Features - Sepal length and petal length
# X = df.iloc[0:100, [1,3]].values # Features - Sepal width and petal width
ppn = Perceptron(eta=0.1, n_iter=10)
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X,y)

# build_learning(X,y)
# print('prediction:',ppn.predict([5.87, 4.63]))


plot_decision_regions(X, y, classifier=ppn)
plotter.xlabel('sepal length [cm]')
plotter.ylabel('petal length [cm]')
plotter.legend(loc='upper left')

plotter.tight_layout()
plotter.show()


