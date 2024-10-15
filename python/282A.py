'''
https://codeforces.com/problemset/problem/282/A
Accepted
93ms
4kb
2024-09-19 22:03:56
'''

x = 0
operations = int(input())
for operation in range(0,operations):
    operationInput = input()
    if operationInput == "X++" or operationInput == "++X":
        x = x + 1
    else:
        x = x - 1

print(x)