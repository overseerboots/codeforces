'''
https://codeforces.com/contest/9/problem/A
Accepted
154 ms
16 KB
2024-12-09 18:27:54
'''

scores = input().split()
win = 0
if int(scores[0]) >= int(scores[1]):
    highest_score = int(scores[0])
else:
    highest_score = int(scores[1])

# All code from this point onwards sucks
if highest_score == 0:
    print("1/1")
elif highest_score == 1:
    print("1/1")
elif highest_score == 2:
    print("5/6")
elif highest_score == 3:
    print("2/3")
elif highest_score == 4:
    print("1/2")
elif highest_score == 5:
    print("1/3")
else:
    print("1/6")