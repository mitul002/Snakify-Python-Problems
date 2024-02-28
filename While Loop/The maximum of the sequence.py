max = 0
pos = 0
while True:
    a = int(input())
    pos += 1
    if a > max:
        max = a
        max_pos = pos

    if a == 0:
        break
print(max_pos)
