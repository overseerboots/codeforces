'''
https://codeforces.com/contest/705/problem/A
Accepted
77 ms
24 KB
2024-12-09 14:47:32
'''

layers = int(input())
output = ""
for x in range(1,layers+1):
    if x % 2 == 0:
        if x != layers:
            output += "I love that "
        else:
            output += "I love it"
    else:
        if x != layers:
            output += "I hate that "
        else:
            output += "I hate it"

print(output)