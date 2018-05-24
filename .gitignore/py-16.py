a=int(input())
b=int(input())
for x in range(a,b):
    if num>1:
        for i in range(2,x):
            if (x%i)==0:
                break
        else:
            print(x)
