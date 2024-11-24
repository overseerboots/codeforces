'''
https://codeforces.com/contest/791/problem/A
Accepted
77ms
28kb
https://codeforces.com/contest/791/problem/A
'''

years = 0

brothers = input().split(" ")
limak, bob = int(brothers[0]), int(brothers[1])
del brothers
while bob >= limak:
	bob *= 2
	limak *= 3
	years += 1
print(years)
