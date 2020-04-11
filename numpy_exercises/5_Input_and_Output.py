
# coding: utf-8

# # Input and Output

# In[1]:


from __future__ import print_function
import numpy as np


np.__version__


# In[4]:


from datetime import date
print(date.today())


# ## NumPy binary files (NPY, NPZ)

# Q1. Save x into `temp.npy` and load it.

# In[5]:


x = np.arange(10)


# Check if there exists the 'temp.npy' file.
import os
if os.path.exists('temp.npy'):
    x2 = ...
    print(np.array_equal(x, x2))


# Q2. Save x and y into a single file 'temp.npz' and load it.

# In[6]:


x = np.arange(10)
y = np.arange(11, 20)
...

with ... as data:
    x2 = data['x']
    y2 = data['y']
    print(np.array_equal(x, x2))
    print(np.array_equal(y, y2))


# ## Text files

# Q3. Save x to 'temp.txt' in string format and load it.

# In[7]:


x = np.arange(10).reshape(2, 5)
header = 'num1 num2 num3 num4 num5'
...
...


# Q4. Save `x`, `y`, and `z` to 'temp.txt' in string format line by line, then load it.

# In[8]:


x = np.arange(10)
y = np.arange(11, 21)
z = np.arange(22, 32)
...
...


# Q5. Convert `x` into bytes, and load it as array.

# In[9]:


x = np.array([1, 2, 3, 4])
x_bytes = ...
x2 = ...
print(np.array_equal(x, x2))


# Q6. Convert `a` into an ndarray and then convert it into a list again.

# In[10]:


a = [[1, 2], [3, 4]]
x = ...
a2 = ...
print(a == a2)


# ## String formatting¶

# Q7. Convert `x` to a string, and revert it.

# In[11]:


x = np.arange(10).reshape(2,5)
x_str = ...
print(x_str, "\n", type(x_str))
x_str = x_str.replace("[", "") # [] must be stripped
x_str = x_str.replace("]", "")
x2 = ...
assert np.array_equal(x, x2)


# ## Text formatting options

# Q8. Print `x` such that all elements are displayed with precision=1, no suppress.

# In[12]:


x = np.random.uniform(size=[10,100])
np.set_printoptions(...)
print(x)


# ## Base-n representations

# Q9. Convert 12 into a binary number in string format.

# In[13]:





# Q10. Convert 12 into a hexadecimal number in string format.

# In[14]:




