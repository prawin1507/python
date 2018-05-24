n=raw_input()
num={'X':10,'V':5,'I':1}
a=0
b=0
for value in (num[c] for c in reversed(n.upper())):
 v=(value,-value)[value<1]
 a+=(value,-value)[value<1]
 b=value
print (a)
