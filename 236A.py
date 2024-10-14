'''
https://codeforces.com/contest/236/problem/A
Accepted
186 ms
36 KB
2024-10-14 19:54:35
'''

used_letters = []
username = input()
for check_letter in range(0,len(username)):
    if username[check_letter] not in used_letters:
        used_letters.append(username[check_letter])
if len(used_letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")