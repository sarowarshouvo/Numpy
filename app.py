import numpy as np

# 1st part

# Creating array
a=np.array([1,2,3])
b=np.array([[9.,8.0,7.0],[2.0,3.0,4.0]])
print(a,b)
# Get dimension
print(a.ndim)
print(b.ndim)
# Get shape
print(a.shape)
print(b.shape)
# Get type
print(a.dtype)
print(b.dtype)
# Get size
print(a.itemsize)
print(b.itemsize)
# Get total size
print(a.nbytes)

# 2nd part

# Getting a specific element
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a[1,4])
print(a[1,-3])
# Getting a specific row
print(a[1,:])
# Getting a specific col
print(a[:,6])
# More fancy [row, startindex:endindex:step]
print(a[0,0:7:2])
# Assigning a value
a[:,2]=5
print(a)
# 3d arrays specific element
a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)
print(a[1,1,:])

# 3rd part

# Creating all 1's matrix
a=np.ones((2,3,3))
print(a)

# Any other number
print(np.full((2,2),10))
# Random decimal numbs
print(np.random.rand(2,2))
# Random int numbs
print(np.random.randint(4,7,size=(2,3)))
# Identity matrix
print(np.identity(3))

# Repeating an arr

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

#  Exercise
# Make this array without declaring each elements
# [  [1,1,1,1,1],
#    [1,0,0,0,1],
#    [1,0,9,0,1],
#    [1,0,0,0,1],
#    [1,1,1,1,1]  ]
a=np.ones((5,5))
print(a)
b=np.zeros((3,3))
print(b)
b[1,1]=9
print(b)
a[1:4,1:4]=b
print(a)

# 4th part

# Coping from one matrix to another
a=[1,2,3]
b=a.copy()
b[1]=20
print(a)
print(b)

# Maths
b=np.array([1,2,3])
print(b+2)
print(b-2)
print(b*2)
print(b/2)
c=np.array([1,0,0])
print(b+c)
print(b**2)

# Linear Algebra

# Matrix multiplication
d=np.ones((2,3))
print(d)
e=np.full((3,2),2)
print(e)
print(np.matmul(d,e))
# Find the determinant
a=np.identity(3)
print(np.linalg.det(a))

# Statistics (min,max,mean)

stat=np.array([[1,2,3,],[4,5,6]])
print(stat.min())
# or
print(np.min(stat))
print(np.max(stat))
print(np.mean(stat))

# Finding Both min values from each row
y=stat.min(axis=1)
print(y)
# Sum
print(np.sum(stat))
# sum of col
z=np.sum(stat,axis=0)
print(z)

# 5th part

# Reorganising array
before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after=before.reshape((4,2))
print(after)

# Vertically stacking matrix
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v=np.vstack([v1,v2])
print(v)
v3=np.vstack([v1,v2,v1,v2])
print(v3)

# Horizontal stack
h1=np.zeros((2,4))
h2=np.ones((2,2))
print(h1,h2)
h=np.hstack([h1,h2])
print(h)

# Part 6

# Miscellaneous

# Load data from file
file_data=np.genfromtxt('data.txt',delimiter=',')
file_data=file_data.astype('int32')
print(file_data)

# Boolean masking and advanced indexing
print(file_data>50)
print(file_data[file_data>50])
a=np.any(file_data>50,axis=0)
print(a)
a=np.all(file_data>50,axis=0)
print(a)
