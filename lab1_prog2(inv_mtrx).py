# python code to find transpose of a matrix

def cofac(a):
	b=len(a)
	cofac=[]
	for i in range(b):
		c=[]
		for j in range(b):
			d=[]
			for k in range(b):
				e=[]
				for l in range(b):
					if(i==k or j==l):
						continue
					e.append(a[k][l])
				if(e!=[]):
					d.append(e)
			if((i+j)%2==0):
				m=1
			else:
				m=-1
			y=det(d)
			c.append(y*m)
		cofac.append(c)
	return cofac
def det(a):
	b=len(a)
	if(b==1):
		f=a[0][0]*1.0
		return f
	elif(b==2):
		f=(a[0][0]*a[1][1]-a[0][1]*a[1][0])*1.0
		return f
	else:
		t=[]
		t=cofac(a)
		f=0.0
		for l in range(b):
			f=f+(a[0][1]*t[0][1])
		return f
def transpose(a):
	b=len(a)
	d=[]
	for j in range(b):
		f=[]
		for i in range (b):
			f.append(a[i][j])
		d.append(f)
	return d
print"enter the matrix format\n[[a11,a12,....a1n],[a21,a22,....,a2n],.....[an1,an2,.....,ann]]"
a=input("enter the elements for matrix A")
b=len(a)
f=det(a)
if(f==0):
	print("inverse doesn't exist")
elif(b==1):
		inverse=[[1.0/a[0][0]]]
		print inverse
else:
	inverse=transpose(cofac(a))
	for i in range(b):
		for j in range(b):
			inverse[i][j]=inverse[i][j]/f
	print inverse
