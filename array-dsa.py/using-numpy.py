import numpy as np
a = np.array([1,2,3,4,5])
z = np.zeros(5)
o = np.ones((2,3))
r = np.arange(0,10,2)
l = np.linspace(0,1,2)
rd = np.random.randint(1,100,6)
print(a)
print(z)
print(o)
print(r)
print(l)
print(rd)
#--Vectorised maths--
a + 10
a * 2
np.sqrt(a)
np.square(a)
np.clip(a,2,4)
print(a+10)
print(a*2)
print(np.sqrt(a))
print(np.square(a))
print(np.clip(a,2,4))
#--statistics--
np.mean(a)
np.std(a)
np.median(a)
np.percentile(a,75)
print(np.mean(a))
print(np.std(a))
print(np.median(a))
print(np.percentile(a,75))
#--shape/Reshape--
a.reshape(5,1)
a.shape 
a.dtype
a.astype(float)
print(a.reshape(5,1))
print(a.shape)
print(a.dtype)
print(a.astype(float))
#--Boolean Indexing--
