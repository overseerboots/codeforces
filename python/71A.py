'''
https://codeforces.com/problemset/problem/71/A
Accepted
77ms
20kb
2024-09-19 18:21:02
'''

wordCount = int(input())
words = ""
for wordNum in range(0,wordCount):
  activeWord = input()
  if len(activeWord) > 10:
    words = words + activeWord[0] + str((len(activeWord)) - 2) + activeWord[len(activeWord)-1] + "\n"
  else:
    words = words + activeWord + "\n"
print(words)