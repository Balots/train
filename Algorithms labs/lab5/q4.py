def perfect_square(n):
    odd = 1
    while n > 1:
        n -= odd
        odd += 2
    if n == 0:
        return True
    return False


ans = []
for i in range(1, int(input()) + 1):
    if perfect_square(int(input())):
        ans += [i]

print(*ans)