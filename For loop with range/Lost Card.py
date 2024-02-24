a=int(input())
sum1=0
for i in range(1,a+1):
    sum1=sum1+i
sum2=0
for i in range(1,a):
    sum2 = sum2 + int(input())

result=sum1-sum2
print(result)