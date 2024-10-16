'''
https://codeforces.com/contest/734/problem/A
Accepted
77ms
16kb
2024-10-16 03:33:07
'''

anton_wins = 0
danik_wins = 0
game_count = int(input())
outcomes = input()
for win_check in range(0,game_count):
    if outcomes[win_check] == "A":
        anton_wins = anton_wins + 1
    else:
        danik_wins = danik_wins + 1
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")