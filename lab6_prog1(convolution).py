import numpy as np
x_array=list()
h_array=list()
a=input("enter length of x array")
b=input("enter length of h array")
for i in range(int(a)):
	m=input("elements=")
	x_array.append(int(m))
print("array",x_array)
for j in range(int(b)):
	n=input("elements=")
	h_array.append(int(n))
print("array",h_array)
y=[]
for n in range(a+b-1):
	sum=0
	for k in range(a):
		if(((n-k)>=0)and((n-k)<b)):
			sum=sum+x_array[k]*h_array[n-k]
	y=np.append(y,sum)
print("resultant convolution is",y)




