import numpy as np

# 1
v = np.array([3, 4])
norm = np.linalg.norm(v)
v_norm = v/norm
norm_v_norm = np.linalg.norm(v_norm)
norm_v_norm_sum = norm_v_norm.sum()

# 2
point1 = np.array([1, 2])
point2 = np.array([4, 6])
di = point1 - point2
di = di**2
distance = di.sum()**0.5

# 3
a = np.array([1, 2])
b = np.array([2, 3])
c = np.array([5, 6])

al = np.linalg.norm(a)
bl = np.linalg.norm(b)
cl = np.linalg.norm(c)

v1 = np.dot(a, b)/(al * bl)
v2 = np.dot(a, c)/(al * cl)
v3 = np.dot(b, c)/(bl * cl)

max_similarity = max([v1, v2, v3])

# 4
a = np.array([1, 0])
b = np.array([1, 1])

cos = np.dot(a, b)/np.linalg.norm(a)/np.linalg.norm(b)
theta = np.arccos(cos)
print(theta)
print('TESTING')
print('TESTING2')