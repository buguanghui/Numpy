
# coding: utf-8

# # Soring, searching, and counting

# In[3]:


import numpy as np


x = np.array([[1,4],[3,1]])
out = np.sort(x, axis=1)
x.sort(axis=1)
assert np.array_equal(out, x)
print out


# Q2. Sort pairs of surnames and first names and return their indices. (first by surname, then by name).

# In[13]:


surnames =    ('Hertz',    'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav')
print np.lexsort((first_names, surnames))


# Q3. Get the indices that would sort x along the second axis.

# In[17]:


x = np.array([[1,4],[3,1]])
out = np.argsort(x, axis=1)
print out


# Q4. Create an array such that its fifth element would be the same as the element of sorted x, and it divide other elements by their value.

# In[48]:


x = np.random.permutation(10)
print "x =", x
print "\nCheck the fifth element of this new array is 5, the first four elements are all smaller than 5, and 6th through the end are bigger than 5\n", 
out = np.partition(x, 5)
x.partition(5) # in-place equivalent
assert np.array_equal(x, out)
print out


# Q5. Create the indices of an array such that its third element would be the same as the element of sorted x, and it divide other elements by their value.

# In[56]:


x = np.random.permutation(10)
print "x =", x
partitioned = np.partition(x, 3)
indices = np.argpartition(x, 3)
print "partitioned =", partitioned
print "indices =", partitioned
assert np.array_equiv(x[indices], partitioned)


# ## Searching

# Q6. Get the maximum and minimum values and their indices of x along the second axis.

# In[78]:


x = np.random.permutation(10).reshape(2, 5)
print "x =", x
print "maximum values =", np.max(x, 1)
print "max indices =", np.argmax(x, 1)
print "minimum values =", np.min(x, 1)
print "min indices =", np.argmin(x, 1)


# Q7. Get the maximum and minimum values and their indices of x along the second axis, ignoring NaNs.

# In[79]:


x = np.array([[np.nan, 4], [3, 2]])
print "maximum values ignoring NaNs =", np.nanmax(x, 1)
print "max indices =", np.nanargmax(x, 1)
print "minimum values ignoring NaNs =", np.nanmin(x, 1)
print "min indices =", np.nanargmin(x, 1)


# Q8. Get the values and indices of the elements that are bigger than 2 in x.
# 

# In[113]:


x = np.array([[1, 2, 3], [1, 3, 5]])
print "Values bigger than 2 =", x[x>2]
print "Their indices are ", np.nonzero(x > 2)
assert np.array_equiv(x[x>2], x[np.nonzero(x > 2)])
assert np.array_equiv(x[x>2], np.extract(x > 2, x))


# Q9. Get the indices of the elements that are bigger than 2 in the flattend x.

# In[4]:


x = np.array([[1, 2, 3], [1, 3, 5]])
print np.flatnonzero(x>2)
assert np.array_equiv(np.flatnonzero(x), x.ravel().nonzero())


# Q10. Check the elements of x and return 0 if it is less than 0, otherwise the element itself.

# In[105]:


x = np.arange(-5, 4).reshape(3, 3)
print np.where(x <0, 0, x)


# Q11. Get the indices where elements of y should be inserted to x to maintain order.

# In[109]:


x = [1, 3, 5, 7, 9]
y = [0, 4, 2, 6]
np.searchsorted(x, y)


# ## Counting

# Q12. Get the number of nonzero elements in x.

# In[120]:


x = [[0,1,7,0,0],[3,0,0,2,19]]
print np.count_nonzero(x)
assert np.count_nonzero(x) == len(x[x!=0])

