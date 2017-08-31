import numpy as np

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L2 loss function defined above
    """
    loss = np.sum(np.dot(y - yhat))

    return loss

#yhat = np.array([.9, 0.2, 0.1, .4, .9])
#y = np.array([1, 0, 0, 1, 1])
#print("L2 = " + str(L2(yhat,y)))

A2 = np.array([[ 0.50154066, 0.49899566, 0.50213783]])
print np.vectorize(lambda T: 1 if(T > 0.5) else 0)(A2)
print A2.shape