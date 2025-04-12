# A Pythagorean triplet is a set of three natural numbers a < b < c for which a^2 + b^2 = c^2
# Given n, check if there exists a Pythagorean triplet for which a + b + c = N
# Find the maximum possible value of a*b*c among all such Pythagorean triplets
# If there's no such triplet, print -1

# Input Format
# The first line contains an integer t (number of test cases)
# The next t lines will contain an integer n

# Constraints:
# 1 <= t <= 3000
# 1 <= n <= 3000

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
