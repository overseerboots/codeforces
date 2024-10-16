'''
https://codeforces.com/contest/116/problem/A
Accepted
218ms
32kb
2024-10-16 17:49:09
'''

passengers = 0
max_passengers = 0
stops = int(input())
for stop in range(0,stops):
    exit_enter = input().split(" ")
    passengers = (passengers - int(exit_enter[0])) + int(exit_enter[1])
    if max_passengers < passengers:
        max_passengers = passengers
print(max_passengers)