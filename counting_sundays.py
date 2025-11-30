# how many sundays fell on the first of the month between two given dates
# other info: 1st Jan 1900 was a Monday
# a leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400

# Input format:
# Each testcase (t) will contain two lines
# Y1 space M1 space D1 on first line denoting starting date
# Y2 space M2 space D2 on second line denoting ending date

# Constraints:
# 1 <= t <= 100
# 1900 <= Y1 <= 1e16
# Y1 <= Y2 <= (Y1 + 1000)
# 1 <= M1, M2 <= 12
# 1 <= D1, D2 <= 31

t = int(input().strip())  # number of test cases
for a0 in range(t):  # range of num of test cases
    dates = input().strip().split("\n")
    date1 = dates[0].split(" ")  # 'tis now in the Y M D format
    date2 = dates[1].split(" ")
    for year in range(int(date1[0]), int(date2[0])):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leap_year = True
            # here, we have taken care of the leap year counting
        for month in range(12):



    # separate math for once we hit the final year
    for month in range(1, int(date2[1])+1):

    # separate math for once we hit the final month
    for day in range(1, int(date2[2]) + 1):



