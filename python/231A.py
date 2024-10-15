'''
https://codeforces.com/problemset/problem/231/A
Accepted
248ms
1392kb
2024-09-19 21:24:53
'''

problemCount = int(input())
viableProblems = 0
sureness = []
for problem in range(0,problemCount):
    opinions = input()
    opinionsList = opinions.split(" ")
    sureness = list(map(int, opinionsList))
    if sum(sureness) > 1:
        viableProblems = viableProblems + 1
print(str(viableProblems))