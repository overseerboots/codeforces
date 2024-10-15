'''
https://codeforces.com/contest/546/problem/A
Accepted
78ms
16kb
2024-10-15 17:11:50
'''

knw = input().split(" ")
banana_cost = int(knw[0])
dollars = int(knw[1])
wanted_bananas = int(knw[2])
for banana_multiplier in range(1,wanted_bananas+1):
    dollars = dollars - banana_cost * banana_multiplier
if dollars > 0:
    print("0")
else:
    print(-dollars)