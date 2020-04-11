
# coding: utf-8

# # Set routines

# In[4]:


import numpy as np




x = np.array([1, 2, 6, 4, 2, 3, 2])
out, indices = np.unique(x, return_inverse=True)
print "unique elements =", out
print "reconstruction indices =", indices
print "reconstructed =", out[indices]


# ## Boolean operations

# Q2. Create a boolean array of the same shape as x. If each element of x is present in y, the result will be True, otherwise False.

# In[19]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1])
print np.in1d(x, y)


# Q3. Find the unique intersection of x and y.

# In[20]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])
print np.intersect1d(x, y)


# Q4. Find the unique elements of x that are not present in y.

# In[21]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])
print np.setdiff1d(x, y)


# Q5. Find the xor elements of x and y.

# In[40]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])
out1 = np.setxor1d(x, y)
out2 = np.sort(np.concatenate((np.setdiff1d(x, y), np.setdiff1d(y, x))))
assert np.allclose(out1, out2)
print out1


# Q6. Find the union of x and y.

# In[42]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])
out1 = np.union1d(x, y)
out2 = np.sort(np.unique(np.concatenate((x, y))))
assert np.allclose(out1, out2)
print np.union1d(x, y)

