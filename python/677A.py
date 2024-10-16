'''
https://codeforces.com/contest/677/problem/A
Accepted
62ms
24kb
2024-10-16 18:07:31
'''

path_width = 0
friends_num_and_fence_height = input().split(" ")
friends_num = int(friends_num_and_fence_height[0])
fence_height = int(friends_num_and_fence_height[1])
friends_heights = input().split(" ")
for friend in range(0,friends_num):
    if int(friends_heights[friend]) > fence_height:
        path_width = path_width + 2
    else:
        path_width = path_width + 1
print(path_width)