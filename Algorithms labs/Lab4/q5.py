p1 = 1/1
p2 = 1/1
N = 4
# x + bx = N
# (b+1)x = N
# x = N/(b+1)
# b = p1/p2 or p2/p1
# x = p1*time or p2*time
# time = x/p1 or x/p2
ex = p1 < p2
time = [1/p1, 1/p2][ex] + (N - 1)//([p2/p1, p1/p2][ex] + 1) * ([p2/p1, p1/p2][ex] + 1)
print(time)