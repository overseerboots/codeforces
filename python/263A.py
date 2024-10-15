'''
https://codeforces.com/contest/263/problem/A
Accepted
154ms
28kb
2024-10-14 05:11:49
'''

grid = []
for askInput in range(0,5):
    line = input().split(" ")
    grid.append(line)
for locate1 in range(0,5):
    for i_locate1 in range(0,5):
        if grid[locate1][i_locate1] == "1":
            diffY = abs(locate1 - 2)
            diffX = abs(i_locate1 - 2)
            print(diffX + diffY)
    else:
        pass