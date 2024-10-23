'''
https://codeforces.com/contest/467/problem/A
Accepted
93ms
32kb
2024-10-23 11:52:27
'''

residents = []
available = 0
num_of_rooms = int(input())
for room_num in range(0,num_of_rooms):
    residents = input().split(" ")
    if (int(residents[0]) + 2) <= int(residents[1]):
        available = available + 1
print(available)