import numpy as np

def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """

    s = 1 / (1 + np.exp(-z))

    return s

w = np.array([[ 0.1124579 ],
     [ 0.23106775]])
b = 1.55930492484
dw = np.array([[ 0.90158428],
      [ 1.76250842]])
db = 0.430462071679

X = np.array([[1,2],[3,4]])
m = X.shape[1]
Y_prediction = np.zeros((1,m))
w = w.reshape(X.shape[0], 1)
A = sigmoid(np.dot(w.T, X) + b)

for i in range(A.shape[1]):
    # Convert probabilities A[0,i] to actual predictions p[0,i]
    if A[0,i] > 0.5:
        np.append(Y_prediction, 1)
        Y_prediction[0][i] = 1
    else:
        Y_prediction[0][i] = 0

assert(Y_prediction.shape == (1, m))

