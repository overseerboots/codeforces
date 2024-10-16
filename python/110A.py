'''
https://codeforces.com/contest/110/problem/A
Accepted
124ms
24kb
2024-10-16 03:15:54
'''

num = input()
lucky_count = 0
for lucky_check in range(0,len(num)):
    if num[lucky_check] == "4" or num[lucky_check] == "7":
        lucky_count = lucky_count + 1
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")