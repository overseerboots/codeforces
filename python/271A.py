'''
https://codeforces.com/contest/271/problem/A
Accepted
248ms
24kb
2024-10-16 18:42:17
'''

def dupe_nums(string_year):
    for num in string_year:
        if string_year.count(num) > 1:
            return False
    return True

year_found = 0
year = int(input())
correct_year = year
while year_found == 0:
    if dupe_nums(str(correct_year)) == False or correct_year == year:
        correct_year = correct_year + 1
    else:
        year_found = 1
print(correct_year)