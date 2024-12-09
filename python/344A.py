magnet_num = int(input())
magnets = ""
groups = 1
for x in range(0,magnet_num):
    magnets += input()

for char_check in range(0, len(magnets)):
    try:
        if magnets[char_check] == magnets[char_check + 1]:
            groups += 1
    except:
        break


print(groups)