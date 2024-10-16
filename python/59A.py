'''
https://codeforces.com/contest/59/problem/A
Accepted
186ms
16kb
2024-10-16 02:47:18
'''

upper_count = 0
word = input()
for upper_check in range(0,len(word)):
    if word[upper_check].isupper() == True:
        upper_count = upper_count + 1
lower_count = -(upper_count - len(word))
if upper_count > lower_count:
    print(word.upper())
else:
    print(word.lower())