# By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms
# Input format: First line contains T that denotes the number of test cases. This is followed by T lines, each
# containing an integer N.

# Constraints:
# 1 <= T <= 1e5
# 10 <= N <= 4e16

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # sum all even fibonacci numbers up till n
    # python function call stack size = 996
    fibonacci_nums = [1, 1]
    fibonacci_even_sum = 0
    k = 2
    current = fibonacci_nums[k-1]
    while current <= n:
        new_term = fibonacci_nums[k-2]+fibonacci_nums[k-1]
        fibonacci_nums.append(new_term)
        if (new_term % 2 == 0) and (new_term < n):
            fibonacci_even_sum += new_term
            # adding new even term to sum if even
        k += 1
        current = fibonacci_nums[k-1]
    # print for each test case
    print(fibonacci_even_sum)
    # success :)
