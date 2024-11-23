'''
https://codeforces.com/contest/158/problem/A
Accepted
154ms
28 KB
2024-11-23 22:25:05
'''

nk = input().split(" ")
n, k = int(nk[0]), int(nk[1])
del nk
output = 0
contestants = input().split(" ")
passing_score = int(contestants[k-1])
for contestant_num in range(0,n):
	if int(contestants[contestant_num]) >= passing_score:
		if int(contestants[contestant_num]) > 0:
			output += 1
print(output)
