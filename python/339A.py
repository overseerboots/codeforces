'''
https://codeforces.com/problemset/problem/339/A
Accepted
124ms
16kb
2024-09-23 00:47:44
'''

integers = input().split("+")
integers = sorted(integers)
output = ""
for pos in range(0,len(integers)):
	output += (integers[pos])
	if (pos+1) != len(integers):
		output += "+"
print(output)
