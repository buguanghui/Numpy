
# coding: utf-8

# # Set routines

# In[4]:


import numpy as np


# In[5]:


np.__version__



x = np.array([1, 2, 6, 4, 2, 3, 2])


# ## Boolean operations

# Q2. Create a boolean array of the same shape as x. If each element of x is present in y, the result will be True, otherwise False.

# In[19]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1])


# Q3. Find the unique intersection of x and y.

# In[20]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])


# Q4. Find the unique elements of x that are not present in y.

# In[21]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])


# Q5. Find the xor elements of x and y.

# In[40]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])


# Q6. Find the union of x and y.

# In[42]:


x = np.array([0, 1, 2, 5, 0])
y = np.array([0, 1, 4])

