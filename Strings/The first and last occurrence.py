word=str(input())

c=(word.count("f"))
if c==1:
    print(word.index("f"))
elif c>1:
    print(word.index("f"),word.rindex("f"))


'''word=str(input())

c=(word.count("f"))
if c==1:
    print(word.index("f"))
elif c>1:
    print(word.index("f"),word.count("f"))'''
