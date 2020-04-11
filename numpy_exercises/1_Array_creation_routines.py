
# coding: utf-8

# # Array creation routines

# ## Ones and zeros

# In[1]:


import numpy as np


# Create a new array of 2*2 integers, without initializing entries.

# In[27]:





# Let X = np.array([1,2,3], [4,5,6], np.int32). 
# Create a new array with the same shape and type as X.

# In[32]:


X = np.array([[1,2,3], [4,5,6]], np.int32)


# Create a 3-D array with ones on the diagonal and zeros elsewhere.

# In[33]:





# In[35]:





# Create a new array of 3*2 float numbers, filled with ones.

# In[36]:





# Let x = np.arange(4, dtype=np.int64). Create an array of ones with the same shape and type as X.

# In[59]:


x = np.arange(4, dtype=np.int64)


# Create a new array of 3*2 float numbers, filled with zeros.

# In[45]:





# Let x = np.arange(4, dtype=np.int64). Create an array of zeros with the same shape and type as X.

# In[58]:


x = np.arange(4, dtype=np.int64)


# Create a new array of 2*5 uints, filled with 6.

# In[49]:





# Let x = np.arange(4, dtype=np.int64). Create an array of 6's with the same shape and type as X.

# In[79]:


x = np.arange(4, dtype=np.int64)


# ## From existing data

# Create an array of [1, 2, 3].

# In[53]:





# Let x = [1, 2]. Convert it into an array.

# In[60]:


x = [1,2]


# Let X = np.array([[1, 2], [3, 4]]). Convert it into a matrix.

# In[62]:


X = np.array([[1, 2], [3, 4]])


# Let x = [1, 2]. Conver it into an array of `float`.

# In[63]:


x = [1, 2]


# Let x = np.array([30]). Convert it into scalar of its single element, i.e. 30.

# In[67]:


x = np.array([30])


# Let x = np.array([1, 2, 3]). Create a array copy of x, which has a different id from x.

# In[76]:


x = np.array([1, 2, 3])


# ## Numerical ranges

# Create an array of 2, 4, 6, 8, ..., 100.

# In[85]:





# Create a 1-D array of 50 evenly spaced elements between 3. and 10., inclusive.

# In[86]:





# Create a 1-D array of 50 element spaced evenly on a log scale between 3. and 10., exclusive.

# In[88]:





# ## Building matrices

# Let X = np.array([[ 0,  1,  2,  3],
#                   [ 4,  5,  6,  7],
#                  [ 8,  9, 10, 11]]).
#                  Get the diagonal of X, that is, [0, 5, 10].

# In[93]:


X = np.array([[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]])


# Create a 2-D array whose diagonal equals [1, 2, 3, 4] and 0's elsewhere.

# In[95]:





# Create an array which looks like below.
# array([[ 0.,  0.,  0.,  0.,  0.],
#        [ 1.,  0.,  0.,  0.,  0.],
#        [ 1.,  1.,  0.,  0.,  0.]])

# In[97]:





# Create an array which looks like below.
# array([[ 0,  0,  0],
#        [ 4,  0,  0],
#        [ 7,  8,  0],
#        [10, 11, 12]])

# In[101]:





# Create an array which looks like below. array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 0,  8,  9],
#        [ 0,  0, 12]])

# In[102]:




