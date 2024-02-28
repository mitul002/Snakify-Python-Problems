count = 0
while True:
    a=int(input())
    if a == 0:
        break
    if a%2==0:
        count =count+ 1
print(count)

'''If we take (if a==0) at last then the loop will apply on 0 also
then 0%2==0 will also be count. so the count variable will increase.
so the program will not work properly
'''