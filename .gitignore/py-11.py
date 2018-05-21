def power(b,E)
 if(E==1):
    return(b)
 if(E!=1):
    return(b*power(b,E-1))
b=int(input("Enter the base number"))
E=int(input("Enter the exponential"))
print(power(b,E))
