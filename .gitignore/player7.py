st=raw_input()
x=list(st)
y=''
for i in range(0,len(st)-1,2)
 t=x[i]
 x[i]=x[i+1]
 x[i+1]=t
 y=y+x[i]+x[i+1]
if(len(st)%2!=0):
 y=y+a[i+2]
print(y) 
 
