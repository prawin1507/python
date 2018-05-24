n=int(input())
if (n<=20):
 fact=1
 for i in range(1,n+1):
  fact=fact*i
 print("Factorial of given number is",fact)
else:
 print("The given number is greater than 20")
 
 
