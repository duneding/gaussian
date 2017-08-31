import numpy as np

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

Y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

# Randomly initialize our weights with mean
weights_0 = 2 * np.random.random((3,4)) - 1
weights_1 = 2 * np.random.random((4,1)) - 1

print weights_0
print weights_1


# Sigmoid - activation function
def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))

# Train the network
for j in range(60000):

    # Feed forward through layers 0, 1, and 2
    layer_0 = X
    layer_1 = nonlin(np.dot(layer_0, weights_0))
    layer_2 = nonlin(np.dot(layer_1, weights_1))

    # Calculate the error
    layer_2_error = Y - layer_2

    if (j % 10000) == 0:
        print "Error:" + str(np.mean(np.abs(layer_2_error)))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    layer_2_delta = layer_2_error * nonlin(layer_2, deriv=True)

    # how much did each k1 value contribute to the k2 error (according to the weights)?
    layer_1_error = layer_2_delta.dot(weights_1.T)

    # in what direction is the target k1?
    # were we really sure? if so, don't change too much.
    layer_1_delta = layer_1_error * nonlin(layer_1, deriv=True)

    weights_1 += layer_1.T.dot(layer_2_delta)
    weights_0 += layer_0.T.dot(layer_1_delta)