x=int(input())

fact=1
sum=0
for i in range(1, int(x)+1):
  fact=fact*i
  sum=sum+fact
print(sum)
