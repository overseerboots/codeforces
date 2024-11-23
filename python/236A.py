'''
https://codeforces.com/contest/236/problem/A
Accepted
156 ms
24 KB
2024-10-14 19:54:35
'''

distinct_character_count = 0
used_chars = []
username = input()
for char in username:
	if char not in used_chars:
		distinct_character_count += 1
		used_chars += char
if distinct_character_count % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")
