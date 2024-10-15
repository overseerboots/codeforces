'''
https://codeforces.com/contest/266/problem/A
Accepted
154ms
12kb
2024-10-15 15:03:33
'''

stones_num = int(input())
stones = input()
stones = stones + "X"
out_num = 0
for check_stones in range(0,stones_num):
    active_stone = stones[check_stones]
    if stones[check_stones+1] == stones[check_stones]:
        out_num = out_num + 1
    elif stones[check_stones+1] == "X":
        break
    else:
        pass
print(out_num)