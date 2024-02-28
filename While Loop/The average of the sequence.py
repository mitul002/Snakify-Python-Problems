count=0
sum=0
while True:
    a=int(input())
    count+=1
    sum+=a
    if a==0:
        break
print(sum/(count-1))