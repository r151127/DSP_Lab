import numpy as np
n=int(input("enter the number of samples"))
x=[]
for i in range(n):
	y=int(input("enter no.of samples")) 
	x=np.append(x,y)
print("enter samples:,")
y=[]
s=0
for i in range(n):
	s=s+x[i]
	y=np.append(y,s)
print("accumulator result:",y)