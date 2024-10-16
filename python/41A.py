'''
https://codeforces.com/contest/41/problem/A
Accepted
77ms
28kb
2024-10-16 03:39:53
'''

word = input()
rev_word = input()
if word[::-1] == rev_word:
    print("YES")
else:
    print("NO")