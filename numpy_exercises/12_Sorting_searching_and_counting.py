
# coding: utf-8

# # Soring, searching, and counting

# In[1]:


import numpy as np


# In[2]:


np.__version__


x = np.array([[1,4],[3,1]])


# Q2. Sort pairs of surnames and first names and return their indices. (first by surname, then by name).

# In[13]:


surnames =    ('Hertz',    'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav')


# Q3. Get the indices that would sort x along the second axis.

# In[17]:


x = np.array([[1,4],[3,1]])


# Q4. Create an array such that its fifth element would be the same as the element of sorted x, and it divide other elements by their value.

# In[48]:


x = np.random.permutation(10)
print "x =", x


# Q5. Create the indices of an array such that its third element would be the same as the element of sorted x, and it divide other elements by their value.

# In[56]:


x = np.random.permutation(10)
print "x =", x


# ## Searching

# Q6. Get the maximum and minimum values and their indices of x along the second axis.

# In[78]:


x = np.random.permutation(10).reshape(2, 5)
print "x =", x


# Q7. Get the maximum and minimum values and their indices of x along the second axis, ignoring NaNs.

# In[79]:


x = np.array([[np.nan, 4], [3, 2]])


# Q8. Get the values and indices of the elements that are bigger than 2 in x.
# 

# In[113]:


x = np.array([[1, 2, 3], [1, 3, 5]])


# Q9. Get the indices of the elements that are bigger than 2 in the flattend x.

# In[100]:


x = np.array([[1, 2, 3], [1, 3, 5]])


# Q10. Check the elements of x and return 0 if it is less than 0, otherwise the element itself.

# In[105]:


x = np.arange(-5, 4).reshape(3, 3)


# Q11. Get the indices where elements of y should be inserted to x to maintain order.

# In[109]:


x = [1, 3, 5, 7, 9]
y = [0, 4, 2, 6]


# ## Counting

# Q12. Get the number of nonzero elements in x.

# In[120]:


x = [[0,1,7,0,0],[3,0,0,2,19]]

