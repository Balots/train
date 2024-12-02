with open('input2') as file:
    nums = file.readline()
    n = int(file.readline())
    ans = [file.readline().split() for _ in range(n)]

print(nums)
print(n)
print(ans)

for v in ans:
    sums = nums[int(v[0]):int(v[1])+1].count('1')
    check = ('odd', 'even')[sums % 2 != 0]
    if check != v[2]:
        print(v, 'not correct')
