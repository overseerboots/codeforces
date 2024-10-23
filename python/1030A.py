'''
https://codeforces.com/contest/1030/problem/A
Accepted
62ms
20kb
2024-10-23 11:42:55
'''

hard = False
num_of_opinions = int(input())
opinions_list = input().split(" ")
for opinion_check in range(0,num_of_opinions):
    if int(opinions_list[opinion_check]):
        hard = True
    else:
        pass
if hard == True:
    print("HARD")
else:
    print("EASY")