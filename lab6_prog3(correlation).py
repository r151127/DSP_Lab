# implementation of correlation of given two signals
import numpy as np
import matplotlib.pyplot as plt
a=[5,2,3]
b=[2,4,1]
def convolution(a,b):
      m=np.size(a)
      n=np.size(b)
      c=np.zeros(m+n-1)
      for i in range(m):
	     for j in range(n):
		c[i+j]=c[i+j]+a[i]*b[j]
      return c

x=list()
p=input("enter length of x=")
for i in range(p):
	m=input("elements=")
	x.append(int(m))
print("array",x)
y=[]
for j in range(p):
	y.append(m-j)

t=convolution(a,b)
print("correlation of two signals is",t) 
plt.plot(t)
plt.show()




