
# coding: utf-8



import numpy as np


# In[3]:


np.__version__


# ## Order statistics

# Q1. Return the minimum value of x along the second axis.

# In[10]:


x = np.arange(4).reshape((2, 2))
print("x=\n", x)


# Q2. Return the maximum value of x along the second axis. Reduce the second axis to the dimension with size one.

# In[12]:


x = np.arange(4).reshape((2, 2))
print("x=\n", x)


# Q3. Calcuate the difference between the maximum and the minimum of x along the second axis.

# In[19]:


x = np.arange(10).reshape((2, 5))
print("x=\n", x)


# Q4. Compute the 75th percentile of x along the second axis.

# In[30]:


x = np.arange(1, 11).reshape((2, 5))
print("x=\n", x)


# ## Averages and variances

# Q5. Compute the median of flattened x.

# In[33]:


x = np.arange(1, 10).reshape((3, 3))
print("x=\n", x)


# Q6. Compute the weighted average of x.

# In[62]:


x = np.arange(5)
weights = np.arange(1, 6)


# Q7. Compute the mean, standard deviation, and variance of x along the second axis.

# In[72]:


x = np.arange(5)
print("x=\n",x)


# ## Correlating

# Q8. Compute the covariance matrix of x and y.

# In[82]:


x = np.array([0, 1, 2])
y = np.array([2, 1, 0])


# Q9. In the above covariance matrix, what does the -1 mean?

# Q10. Compute Pearson product-moment correlation coefficients of x and y.

# In[87]:


x = np.array([0, 1, 3])
y = np.array([2, 4, 5])


# Q11. Compute cross-correlation of x and y.

# In[90]:


x = np.array([0, 1, 3])
y = np.array([2, 4, 5])


# ## Histograms

# Q12. Compute the histogram of x against the bins.

# In[105]:


x = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("ans=\n", ...)

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(x, bins=bins)
plt.show()


# Q13. Compute the 2d histogram of x and y.

# In[127]:


xedges = [0, 1, 2, 3]
yedges = [0, 1, 2, 3, 4]
x = np.array([0, 0.1, 0.2, 1., 1.1, 2., 2.1])
y = np.array([0, 0.1, 0.2, 1., 1.1, 2., 3.3])
...

plt.scatter(x, y)
plt.grid()


# Q14. Count number of occurrences of 0 through 7 in x.

# In[129]:


x = np.array([0, 1, 1, 3, 2, 1, 7])


# Q15. Return the indices of the bins to which each value in x belongs.

# In[130]:


x = np.array([0.2, 6.4, 3.0, 1.6])
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])

