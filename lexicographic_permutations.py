# What is the Nth lexicographic permutation of abcdefghijklm?

# Characteristics of lexicographic permutations:
# they keep each letter at the beginning for (n-1)! permutations
# and same for the next smallest - largest letter
# now, how do we decode which letter should be where provided the number N for the nth permutation
# we must be very careful because N can very well range from 1 to 13! and border cases will be tested

import math
"""
How the heck do we get the configuration from the number of the permutation? Note that this is only possible with
the lexicographic permutation algorithm and won't work for any other methods to generate permutations.
13! = 6227020800
12! = 479001600
8! = 40320
If we can somehow encode the position of each letter and lock it to a certain number of permutations, ex: 5, then
the problem becomes much more solvable. What math shall we do on N?
"""
position_values = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g",
                   8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m"}

factorial_values = {x: math.factorial(x) for x in range(1, 14)}
# factorial_values = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320,
#                     9: 362880, 10: 3628800, 11: 39916800, 12:479001600, 13: 6227020800}
the_permutation = []  # array of chars to join
n_str = input("permutation count: ")
n = int(n_str.strip())
for i in range(12, -1, 1):
    if n > factorial_values[i]:
        the_permutation.append(position_values[i+1])
        n /= (i+1)

print(the_permutation)