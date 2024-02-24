word = input(str())
l = len(word)

if (l % 2 == 0):
    print(word[l // 2:l] + word[0:l // 2])

else:
    print(word[(l // 2) + 1:l] + word[0:(l // 2) + 1])