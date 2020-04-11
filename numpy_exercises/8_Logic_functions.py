
# coding: utf-8

# # Logic functions

# In[1]:


import numpy as np


# In[2]:


np.__version__


# ## Truth value testing
# 

# Q1. Let x be an arbitrary array. Return True if none of the elements of x is zero. Remind that 0 evaluates to False in python.
# 

# In[4]:


x = np.array([1,2,3])
#

x = np.array([1,0,3])
#


# Q2. Let x be an arbitrary array. Return True if any of the elements of x is non-zero.

# In[5]:


x = np.array([1,0,0])
#

x = np.array([0,0,0])
#


# ## Array contents
# 

# Q3. Predict the result of the following code.

# In[8]:


x = np.array([1, 0, np.nan, np.inf])
#print np.isfinite(x)


# Q4. Predict the result of the following code.

# In[10]:


x = np.array([1, 0, np.nan, np.inf])
#print np.isinf(x)


# Q5. Predict the result of the following code.

# In[12]:


x = np.array([1, 0, np.nan, np.inf])
#print np.isnan(x)


# ## Array type testing

# Q6. Predict the result of the following code.

# In[15]:


x = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
#print np.iscomplex(x)


# Q7. Predict the result of the following code.

# In[18]:


x = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
#print np.isreal(x)


# Q8. Predict the result of the following code.

# In[21]:


#print np.isscalar(3)
#print np.isscalar([3])
#print np.isscalar(True)


# ## Logical operations

# Q9. Predict the result of the following code.

# In[31]:


#print np.logical_and([True, False], [False, False])
#print np.logical_or([True, False, True], [True, False, False])
#print np.logical_xor([True, False, True], [True, False, False])
#print np.logical_not([True, False, 0, 1])


# ## Comparison

# Q10. Predict the result of the following code.

# In[42]:


#print np.allclose([3], [2.999999])
#print np.array_equal([3], [2.999999])


# Q11. Write numpy comparison functions such that they return the results as you see.

# In[51]:


x = np.array([4, 5])
y = np.array([2, 5])
#
#
#
#


# Q12. Predict the result of the following code.

# In[50]:


#print np.equal([1, 2], [1, 2.000001])
#print np.isclose([1, 2], [1, 2.000001])

