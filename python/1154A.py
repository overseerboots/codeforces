'''
https://codeforces.com/contest/1154/problem/A
Accepted
77 ms
8 KB
2024-12-09 18:58:04
'''

a = list(map(int, input().split()))
a.sort()
print(a[3] - a[0], a[3] - a[1], a[3] - a[2])
