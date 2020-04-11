
# coding: utf-8

# # Array creation routines

# ## Ones and zeros

# In[1]:


import numpy as np


# Create a new array of 2*2 integers, without initializing entries.

# In[27]:


np.empty([2,2], int)


# Let X = np.array([1,2,3], [4,5,6], np.int32). 
# Create a new array with the same shape and type as X.

# In[32]:


X = np.array([[1,2,3], [4,5,6]], np.int32)
np.empty_like(X)


# Create a 3-D array with ones on the diagonal and zeros elsewhere.

# In[33]:


np.eye(3)


# In[35]:


np.identity(3)


# Create a new array of 3*2 float numbers, filled with ones.

# In[36]:


np.ones([3,2], float)


# Let x = np.arange(4, dtype=np.int64). Create an array of ones with the same shape and type as X.

# In[59]:


x = np.arange(4, dtype=np.int64)
np.ones_like(x)


# Create a new array of 3*2 float numbers, filled with zeros.

# In[45]:


np.zeros((3,2), float)


# Let x = np.arange(4, dtype=np.int64). Create an array of zeros with the same shape and type as X.

# In[58]:


x = np.arange(4, dtype=np.int64)
np.zeros_like(x)


# Create a new array of 2*5 uints, filled with 6.

# In[49]:


np.full((2, 5), 6, dtype=np.uint)


# In[50]:


np.ones([2, 5], dtype=np.uint) * 6


# Let x = np.arange(4, dtype=np.int64). Create an array of 6's with the same shape and type as X.

# In[79]:


x = np.arange(4, dtype=np.int64)
np.full_like(x, 6)


# In[81]:


np.ones_like(x) * 6


# ## From existing data

# Create an array of [1, 2, 3].

# In[53]:


np.array([1, 2, 3])


# Let x = [1, 2]. Convert it into an array.

# In[60]:


x = [1,2]
np.asarray(x)


# Let X = np.array([[1, 2], [3, 4]]). Convert it into a matrix.

# In[62]:


X = np.array([[1, 2], [3, 4]])
np.asmatrix(X)


# Let x = [1, 2]. Conver it into an array of `float`.

# In[63]:


x = [1, 2]
np.asfarray(x)


# In[64]:


np.asarray(x, float)


# Let x = np.array([30]). Convert it into scalar of its single element, i.e. 30.

# In[67]:


x = np.array([30])
np.asscalar(x)


# In[68]:


x[0]


# Let x = np.array([1, 2, 3]). Create a array copy of x, which has a different id from x.

# In[76]:


x = np.array([1, 2, 3])
y = np.copy(x)
print id(x), x
print id(y), y


# ## Numerical ranges

# Create an array of 2, 4, 6, 8, ..., 100.

# In[85]:


np.arange(2, 101, 2)


# Create a 1-D array of 50 evenly spaced elements between 3. and 10., inclusive.

# In[86]:


np.linspace(3., 10, 50)


# Create a 1-D array of 50 element spaced evenly on a log scale between 3. and 10., exclusive.

# In[88]:


np.logspace(3., 10., 50, endpoint=False)


# ## Building matrices

# Let X = np.array([[ 0,  1,  2,  3],
#                   [ 4,  5,  6,  7],
#                  [ 8,  9, 10, 11]]).
#                  Get the diagonal of X, that is, [0, 5, 10].

# In[93]:


X = np.array([[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]])
np.diag(X)


# In[94]:


X.diagonal()


# Create a 2-D array whose diagonal equals [1, 2, 3, 4] and 0's elsewhere.

# In[95]:


np.diagflat([1, 2, 3, 4])


# Create an array which looks like below.
# array([[ 0.,  0.,  0.,  0.,  0.],
#        [ 1.,  0.,  0.,  0.,  0.],
#        [ 1.,  1.,  0.,  0.,  0.]])

# In[97]:


np.tri(3, 5, -1)


# Create an array which looks like below.
# array([[ 0,  0,  0],
#        [ 4,  0,  0],
#        [ 7,  8,  0],
#        [10, 11, 12]])

# In[101]:


np.tril(np.arange(1, 13).reshape(4, 3), -1)


# Create an array which looks like below. array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 0,  8,  9],
#        [ 0,  0, 12]])

# In[102]:


np.triu(np.arange(1, 13).reshape(4, 3), -1)

