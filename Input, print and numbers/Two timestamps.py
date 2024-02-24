h1=int(input())
m1=int(input())
s1=int(input())

h2=int(input())
m2=int(input())
s2=int(input())

h=((h2-h1)*3600)
m=((m2-m1)*60)
s=(s2-s1)

print(h+m+s)



'''
OR

hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
print(hours_2 * 3600 + minutes_2 * 60 + seconds_2
    - hours_1 * 3600 - minutes_1 * 60 - seconds_1)


OR,'''