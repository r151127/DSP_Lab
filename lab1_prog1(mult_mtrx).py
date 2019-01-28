# python program for multiplication of two matrices

print"enter the matrix format\n[[a11,a12,....a1n],[a21,a22,....,a2n],.....[an1,an2,.....,ann]]"
a=input("enter the elements for matrix A")
b=input("enter the elements for matrix B")
p=len(a)
q=len(a[0])
m=len(b)
n=len(b[0])
c=[]
for i in range(p):
	if(q!=m):
		print("matrix multiplication is not possible")
	d=[]
	for j in range(n):
		s=0
		for k in range(m):
			s=s+(a[i][k]*b[k][j])
		d.append(s)
	c.append(d)
print c
