# convolution of two signals using functions
import numpy as np
def convolution(a,b):
      m=np.size(a)
      n=np.size(b)
      c=np.zeros(m+n-1)
      for i in range(m):
	     for j in range(n):
		c[i+j]=c[i+j]+a[i]*b[j]
      return c
x=input("enter x values=")
h=input("enter h values=")
t=convolution(x,h)
print("convolution of two signals is",t)

