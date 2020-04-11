
# coding: utf-8

# # Random Sampling

# In[2]:


import numpy as np


# In[3]:


np.__version__


# In[5]:

np.random.rand(3, 2) 
# Or np.random.random((3,2))


# Q2. Create an array of shape (1000, 1000) and populate it with random samples from a standard normal distribution. And verify that the mean and standard deviation is close enough to 0 and 1 repectively.

# In[42]:


out1 = np.random.randn(1000, 1000)
out2 = np.random.standard_normal((1000, 1000))
out3 = np.random.normal(loc=0.0, scale=1.0, size=(1000, 1000))
assert np.allclose(np.mean(out1), np.mean(out2), atol=0.1)
assert np.allclose(np.mean(out1), np.mean(out3), atol=0.1)
assert np.allclose(np.std(out1), np.std(out2), atol=0.1)
assert np.allclose(np.std(out1), np.std(out3), atol=0.1)
print np.mean(out3)
print np.std(out1)


# Q3. Create an array of shape (3, 2) and populate it with random integers ranging from 0 to 3 (inclusive) from a discrete uniform distribution.

# In[44]:


np.random.randint(0, 4, (3, 2))


# Q4. Extract 1 elements from x randomly such that each of them would be associated with probabilities .3, .5, .2. Then print the result 10 times.

# In[58]:


x = [b'3 out of 10', b'5 out of 10', b'2 out of 10']


# In[60]:


for _ in range(10):
    print np.random.choice(x, p=[.3, .5, .2])


# Q5. Extract 3 different integers from 0 to 9 randomly with the same probabilities.

# In[66]:


np.random.choice(10, 3, replace=False)


# ## Permutations

# Q6. Shuffle numbers between 0 and 9 (inclusive).

# In[86]:


x = np.arange(10)
np.random.shuffle(x)
print x


# In[88]:


# Or
print np.random.permutation(10)


# ## Random generator

# Q7. Assign number 10 to the seed of the random generator so that you can get the same value next time.

# In[91]:


np.random.seed(10)

