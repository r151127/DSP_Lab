import numpy as NP
import matplotlib.pyplot as MP
fs=8000
f=10
sample=8000
x=NP.arange(sample)
y=NP.sin(2*NP.pi*f*x/fs)
z=NP.cos(2*NP.pi*f*x/fs)
s=y-z
MP.subplot(1,3,1)
MP.plot(x,y)
MP.xlabel('sample(n)')
MP.ylabel('voltage(v)')
MP.title("sin wave")
MP.subplot(1,3,2)
MP.plot(x,z)
MP.xlabel('sample(n)')
MP.ylabel('voltage(v)')
MP.title("cos wave")
MP.subplot(1,3,3)
MP.plot(x,s)
MP.xlabel('sample(n)')
MP.ylabel('voltage(v)')
MP.title("result wave")
MP.show()



