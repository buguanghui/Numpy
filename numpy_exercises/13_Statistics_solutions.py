
# coding: utf-8

# # Statistics


import numpy as np


# In[3]:


np.__version__


# ## Order statistics

# Q1. Return the minimum value of x along the second axis.

# In[10]:


x = np.arange(4).reshape((2, 2))
print("x=\n", x)
print("ans=\n", np.amin(x, 1))


# Q2. Return the maximum value of x along the second axis. Reduce the second axis to the dimension with size one.

# In[12]:


x = np.arange(4).reshape((2, 2))
print("x=\n", x)
print("ans=\n", np.amax(x, 1, keepdims=True))


# Q3. Calcuate the difference between the maximum and the minimum of x along the second axis.

# In[19]:


x = np.arange(10).reshape((2, 5))
print("x=\n", x)

out1 = np.ptp(x, 1)
out2 = np.amax(x, 1) - np.amin(x, 1)
assert np.allclose(out1, out2)
print("ans=\n", out1)


# Q4. Compute the 75th percentile of x along the second axis.

# In[30]:


x = np.arange(1, 11).reshape((2, 5))
print("x=\n", x)

print("ans=\n", np.percentile(x, 75, 1))


# ## Averages and variances

# Q5. Compute the median of flattened x.

# In[33]:


x = np.arange(1, 10).reshape((3, 3))
print("x=\n", x)

print("ans=\n", np.median(x))


# Q6. Compute the weighted average of x.

# In[62]:


x = np.arange(5)
weights = np.arange(1, 6)

out1 = np.average(x, weights=weights)
out2 = (x*(weights/weights.sum())).sum()
assert np.allclose(out1, out2)
print(out1)


# Q7. Compute the mean, standard deviation, and variance of x along the second axis.

# In[72]:


x = np.arange(5)
print("x=\n",x)

out1 = np.mean(x)
out2 = np.average(x)
assert np.allclose(out1, out2)
print("mean=\n", out1)

out3 = np.std(x)
out4 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(out3, out4)
print("std=\n", out3)

out5 = np.var(x)
out6 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(out5, out6)
print("variance=\n", out5)


# ## Correlating

# Q8. Compute the covariance matrix of x and y.

# In[82]:


x = np.array([0, 1, 2])
y = np.array([2, 1, 0])

print("ans=\n", np.cov(x, y))


# Q9. In the above covariance matrix, what does the -1 mean?

# It means `x` and `y` correlate perfectly in opposite directions.

# Q10. Compute Pearson product-moment correlation coefficients of x and y.

# In[87]:


x = np.array([0, 1, 3])
y = np.array([2, 4, 5])

print("ans=\n", np.corrcoef(x, y))


# Q11. Compute cross-correlation of x and y.

# In[90]:


x = np.array([0, 1, 3])
y = np.array([2, 4, 5])

print("ans=\n", np.correlate(x, y))


# ## Histograms

# Q12. Compute the histogram of x against the bins.

# In[105]:


x = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("ans=\n", np.histogram(x, bins))

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
H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
print("ans=\n", H)

plt.scatter(x, y)
plt.grid()


# Q14. Count number of occurrences of 0 through 7 in x.

# In[129]:


x = np.array([0, 1, 1, 3, 2, 1, 7])
print("ans=\n", np.bincount(x))


# Q15. Return the indices of the bins to which each value in x belongs.

# In[130]:


x = np.array([0.2, 6.4, 3.0, 1.6])
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])

print("ans=\n", np.digitize(x, bins))

