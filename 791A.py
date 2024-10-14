'''
https://codeforces.com/contest/791/problem/A
Accepted
77ms
28kb
2024-10-14 20:12:26
'''

bear_weights = input().split(" ")
years = 0
limak = int(bear_weights[0])
bob = int(bear_weights[1])
while limak <= bob:
    limak = limak * 3
    bob = bob * 2
    years = years + 1
print(years)