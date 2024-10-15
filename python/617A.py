'''
https://codeforces.com/contest/617/problem/A
Accepted
108ms
20kb
2024-10-15 15:51:40
'''

distance = int(input())
steps = 0
for step_size in range(5,0,-1):
    big_step = 1
    while big_step == 1:
        if distance >= step_size:
            distance = distance - step_size
            steps = steps + 1
        else:
            big_step = 0
print(steps)