import numpy as np

# 1
A = np.array([[1, 3, 5, 8],
              [6, 9, 3, 4],
              [3, 4, 4, 9]])
w = np.array([0.4, 0.1, 0.6, 0.2])

result = A.dot(w)

# 2

arr = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
new_arr = np.reshape(arr, (3, 3))


# 3

Z = np.array([[0.22, 0.64, 0.7, 0.59, 0.75],
              [0.21, 0.11, 0.78, 0.4, 0.95],
              [0.27, 0.43, 0.79, 0.78, 0.72],
              [0.45, 0.29, 0.03, 0.14, 0.39],
              [0.8, 0.21, 0.38, 0.31, 0.48]])

Z_normilized = Z/np.linalg.norm(Z, axis=0)
sum_Z_normilized = sum([np.linalg.norm(x) for x in Z_normilized])

# 4
A = np.array([[[ 0, 1, 2],
               [ 3, 4, 5],
               [ 6, 7, 8],
               [ 9, 10, 11],
               [12, 13, 14]],
              [[15, 16, 17],
               [18, 19, 20],
               [21, 22, 23],
               [24, 25, 26],
               [27, 28, 29]],
              [[30, 31, 32],
               [33, 34, 35],
               [36, 37, 38],
               [39, 40, 41],
               [42, 43, 44]],
              [[45, 46, 47],
               [48, 49, 50],
               [51, 52, 53],
               [54, 55, 56],
               [57, 58, 59]],
              [[60, 61, 62],
               [63, 64, 65],
               [66, 67, 68],
               [69, 70, 71],
               [72, 73, 74]]])

B = np.array([[2., 2., 2., 2., 2.],
              [2., 2., 2., 2., 2.],
              [2., 2., 2., 2., 2.],
              [2., 2., 2., 2., 2.],
              [2., 2., 2., 2., 2.]])

C = B.dot(A)


# 5

def dist(p1, p2):
    point1 = np.array(p1)
    point2 = np.array(p2)
    di = point1 - point2
    di = di ** 2
    return di.sum() ** 0.5

Z = np.array([[ 0, 0],
              [ 3, 4],
              [ 6, 8],
              [ 9, 12],
              [12, 16]])
D = []

for x in Z:
    for y in Z:
        D.append([dist(x, y)])

D = np.array(D).reshape(5, 5)
print(D)
