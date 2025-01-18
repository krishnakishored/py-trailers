# %% [markdown]
# # Load in Numpy ($ pip install numpy)
#

# %%
import numpy as np

# %% [markdown]
# ## The Basics

# %%
# a = np.array([1, 2, 3])
# specify the datatype, default is int64
a = np.array([1, 2, 3], dtype="int16")
print("a = ", a)
b = np.array([[1, 2, 3], [4, 5, 6]], dtype="int16")
print("b = ", b)
c = np.array(
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype="int16"
)
print("c = ", c)

# Get Dimension
print(
    f"Dimension of a: {a.ndim}",
    f"Dimension of b: {b.ndim}",
    f"Dimension of c: {c.ndim}",
)
# Get Shape
print(
    f"Shape of a: {a.shape}",
    f"Shape of b: {b.shape}",
    f"Shape of c: {c.shape}",
)
# Get Type
print(
    f"Type of a: {a.dtype}", f"Type of b: {b.dtype}", f"Type of c: {c.dtype}"
)
# Get Itemsize
print(
    f"Itemsize of a: {a.itemsize}",
    f"Itemsize of b: {b.itemsize}",
    f"Itemsize of c: {c.itemsize}",
)
# Get Size
print(f"Size of a: {a.size}", f"Size of b: {b.size}", f"Size of c: {c.size}")
# Get Total Size
print(
    f"Total Size of a: {a.size * a.itemsize}",
    f"Total Size of b: {b.size * b.itemsize}",
    f"Total Size of c: {c.size * c.itemsize}",
)

# %% [markdown]
# ## Accessing/Changing specific elements, rows, columns, etc
#

# %%
a = np.array(
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    ],
    dtype="int16",
)
print("a = ", a)
# Get a specific element [r, c]
print(a[1, 4])
print(a[-1, -6])  # negative indexing also works
# Get a segment [startindex:endindex:stepsize]
print(a[0, 1:6:2])
## Accessing a 3D array
b = np.array(
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype="int16"
)
print("b = ", b, "shape = ", b.shape)
# set a specific element
b[0, 1, 1] = 2000
print("b = ", b)
# Get a specific element (work outside in)
print("specific element:", b[0, 1, 1])

# set a segment [startindex:endindex:stepsize]
b[:, 1, :] = [[100, 101, 102], [103, 104, 105]]
print("b = ", b)

# %% [markdown]
# ## Initializing Different Types of Arrays
#

# %%
# All 0s matrix
print(np.zeros((2, 3, 2)))
# All 1s matrix
print(np.ones((2, 3, 2)))
# Any other number
print(np.full((2, 2), 99, dtype="float32"))
# Any other number (full_like)
print(np.full_like(a, 4))
# Random decimal numbers
print(np.random.rand(4, 2))
# Random Sample
print("shape of a:", a.shape)
print(np.random.random_sample(a.shape))
# Random Integer values
print(np.random.randint(7, size=(3, 3)))
# The identity matrix
print(np.identity(3))
# Repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

## Challenge
output = np.ones((5, 5), dtype="int16")
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:4, 1:4] = z
print(output)


# %% [markdown]
# ## Be careful when copying arrays!

# %%
l = np.array([1, 2, 3])
print(l)
# m = l # this will create a reference to l
m = l.copy()
m[0] = 100
print("l = ", l)
print("m = ", m)

# %% [markdown]
# ## Mathematics

# %%
a = np.array([1, 2, 3, 4], dtype="float32")
# a /= 2
# a += 2
a *= 2
# a -= 2
print(a)
# Take the sin, cos, tan
print("sin:", np.sin(a), "cos:", np.cos(a), "tan:", np.tan(a))


# %% [markdown]
# ## Linear Algebra
# ref: https://docs.scipy.org/doc/scipy/reference/linalg.html

# %%
a = np.ones((2, 3))
b = np.full((3, 2), 2)
# a*b # ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
print(np.matmul(a, b))
# find the determinant
c = np.identity(3)
print(np.linalg.det(c))

# %% [markdown]
# ## Statistics

# %%
stats = np.array([[1, 2, 3], [4, 5, 6]])
print("min:", np.min(stats))
print(np.max(stats, axis=1))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))

# %% [markdown]
# ## Reorganizing Arrays

# %%
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
after = before.reshape((2, 2, 2))
print(after)

## Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack([v1, v2, v1, v2]))
## Horizontal  stack
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))
print(np.hstack([h1, h2]))


# %% [markdown]
# ## Miscellaneous

# %%
# Load data from file
filedata = np.genfromtxt("data.txt", delimiter=",")
filedata = filedata.astype("int32")
print(filedata)
# Boolean Masking and Advanced Indexing
print(filedata > 50)
print(filedata[filedata > 50])
# You can index with a list in NumPy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])
# Any value greater than 50
print(np.any(filedata > 50, axis=0))
# All values greater than 50
print(np.all(filedata > 50, axis=0))


# %% [markdown]
#
