'''
https://codeforces.com/problemset/problem/339/A
Accepted
154ms
16kb
2024-09-23 00:47:44
'''

equation = input().split("+")
equation = [int(number) for number in equation]
equation.sort()
output = ""
for item in range(0,len(equation)):
    output = output + str(equation[item]) + "+"
output = output[:-1]
print(output)