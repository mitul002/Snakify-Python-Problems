n = int(input())
i = 1
largest = 0
while i <= n:
    if 2**i <=n:
        largest = i
    i += 1
print(largest, 2**largest)