import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])

print A

cal = A.sum(axis=0)
print cal

percentage = 100 * A / cal.reshape(1, 4)
print percentage

a = np.random.randn(4, 3) # a.shape = (4, 3)
b = np.random.randn(3, 2) # b.shape = (3, 2)
#c = a*b #fail

a = np.random.randn(12288, 150) # a.shape = (12288, 150)
b = np.random.randn(150, 45) # b.shape = (150, 45)
c = np.dot(a,b)
xxds = c.a
# aa.shape = (3,4)
# bb.shape = (4,1)
aa = np.random.randn(3, 4)
bb = np.random.randn(4, 1)

zzz = np.zeros((3,4))
for i in range(3):
    for j in range(4):
        zzz[i][j] = aa[i][j] + bb[j]

zz = aa.T + bb
#zz = aa + bb
zz = aa + bb.T
#zz = aa.T + bb.T

a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b


image = np.array([[[ 0.67826139,  0.29380381],
                   [ 0.90714982,  0.52835647],
                   [ 0.4215251 ,  0.45017551]],

                  [[ 0.92814219,  0.96677647],
                   [ 0.85304703,  0.52351845],
                   [ 0.19981397,  0.27417313]],

                  [[ 0.60659855,  0.00533165],
                   [ 0.10820313,  0.49978937],
                   [ 0.34144279,  0.94630077]]])


#v = image.reshape(image[0]*image[1]*image[2], 1)

x = np.array([[0, 3, 4],
             [2, 6, 4]])

__x__ = np.linalg.norm(x,axis=1,keepdims=True)

x_normalized = x / __x__



