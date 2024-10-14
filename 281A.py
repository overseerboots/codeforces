'''
https://codeforces.com/contest/281/problem/A
Accepted
154ms
24kb
2024-10-14 13:42:41
'''

word = input()
word = word[::-1]
char = word[len(word)-1]
char = char.upper()
word = word[:-1]
word = word + char
word = word[::-1]
print(word)