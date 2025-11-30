# some decimal numbers are palindromes in also binary
# find the sum of all natural numbers less than N which are palindromic in base 10 and base K
# input is formatted as "N K"
# 2 <= K <= 9

# I just felt a wave of bliss when I realized that for once I don't have to code in C
# trauma from the last few months is being cured
# thanks BDFL, love ya
what_they_said = input().split(" ")
N, K = int(what_they_said[0]), int(what_they_said[1])  # oh my god I love this language I'm crying


def is_palindrome(s: str) -> bool:
    # omg what... I love pattern matching
    return s == s[::-1]


def convert_base(number_10: int, base: int) -> str:
    # specifically for bases < 10
    if number_10 == 0:
        return "0"
    digits = []
    while number_10:
        digits.append(str(number_10 % base))
        number_10 //= base
    return "".join(reversed(digits))  # doki doki awesomeness


palindromes_10 = []
for i in range(1, N + 1):
    if is_palindrome(str(i)):
        palindromes_10.append(i)

double_base_palindromes = []
for number in palindromes_10:
    converted = convert_base(number, K)  # this is a string
    if is_palindrome(converted):
        double_base_palindromes.append(number)

print(sum(double_base_palindromes))
# success :)
