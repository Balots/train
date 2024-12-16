maxint = 10000000000000000000000000000000000000000000000


def maxSubArraySum(a, size):
    max_sum = -maxint - 1
    end = 0

    for i in range(0, size):
        end = end + a[i]
        max_sum = (max_sum, end)[max_sum < end]
        end = (end, 0)[end < 0]
    return max_sum


# Driver function to check the above function
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))
