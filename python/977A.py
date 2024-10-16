'''
https://codeforces.com/contest/977/problem/A
Accepted
62ms
12kb
2024-10-16 03:05:13
'''

num_and_sub_count = input().split(" ")
num = int(num_and_sub_count[0])
sub_count = int(num_and_sub_count[1])
for subbing in range(0,sub_count):
    if int(str(num)[len(str(num))-1]) > 0: # there has to be a better way to do this
        num = num -1
    else:
        num = int(str(num)[:-1])
print(num)