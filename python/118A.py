'''
https://codeforces.com/contest/118/problem/A
Accepted
154 ms
20 KB
2024-12-09 13:29:16
'''

string = list(input())
vowels = ["A","O","Y","E","U","I","a","o","y","e","u","i"]
for character_num in range(0,len(string)):
    for item in vowels:
        if item in string:
            string.remove(item)


output = ""
for character in string:
    output += "."
    output += character
output = output.lower()
print(output)