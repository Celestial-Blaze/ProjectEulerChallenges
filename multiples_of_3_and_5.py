import math

# code for hackerrank's Euler Challenge 1
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    multiples = set()
    my_n = 1
    for x3 in range(1, math.ceil(n / 3)):
        mult3 = 3 * x3
        multiples.add(mult3)
    for x5 in range(1, math.ceil(n / 5)):
        mult5 = 5 * x5
        multiples.add(mult5)

    sum_of_multiples = sum(multiples)
    print(sum_of_multiples)
