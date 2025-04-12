# sum of the squares of the first n natural numbers = 1^2 + 2^2 + 3^2 + ... + (n-1)^2 + n^2
# square of the sum of the first n natural numbers = (1 + 2 + 3 + ... + n-1 + n)^2
# we need to find the absolute difference between the two

# constraints
# 1 <= t <= 1e4
# 1 <= n <= 1e4

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n_sum = int((n*(n+1))/2)
    sum_of_squares = 0
    for x in range(1, n+1):
        sum_of_squares += x**2
    square_of_sum = n_sum**2
    abs_diff = abs(square_of_sum - sum_of_squares)
    print(abs_diff)
    # success :)
