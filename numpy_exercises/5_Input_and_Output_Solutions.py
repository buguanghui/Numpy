
# coding: utf-8

# # Input and Output

# In[1]:


from __future__ import print_function
import numpy as np

from datetime import date
print(date.today())


# ## NumPy binary files (NPY, NPZ)

# Q1. Save x into `temp.npy` and load it.

# In[4]:


x = np.arange(10)
np.save('temp.npy', x) # Actually you can omit the extension. If so, it will be added automatically.

# Check if there exists the 'temp.npy' file.
import os
if os.path.exists('temp.npy'):
    x2 = np.load('temp.npy')
    print(np.array_equal(x, x2))


# Q2. Save x and y into a single file 'temp.npz' and load it.

# In[5]:


x = np.arange(10)
y = np.arange(11, 20)
np.savez('temp.npz', x=x, y=y)
# np.savez_compressed('temp.npz', x=x, y=y) # If you want to save x and y into a single file in compressed .npz format.
with np.load('temp.npz') as data:
    x2 = data['x']
    y2 = data['y']
    print(np.array_equal(x, x2))
    print(np.array_equal(y, y2))


# ## Text files

# Q3. Save x to 'temp.txt' in string format and load it.

# In[6]:


x = np.arange(10).reshape(2, 5)
header = 'num1 num2 num3 num4 num5'
np.savetxt('temp.txt', x, fmt="%d", header=header) 
np.loadtxt('temp.txt')


# Q4. Save `x`, `y`, and `z` to 'temp.txt' in string format line by line, then load it.

# In[7]:


x = np.arange(10)
y = np.arange(11, 21)
z = np.arange(22, 32)
np.savetxt('temp.txt', (x, y, z), fmt='%d')
np.loadtxt('temp.txt')


# Q5. Convert `x` into bytes, and load it as array.

# In[8]:


x = np.array([1, 2, 3, 4])
x_bytes = x.tostring() # Don't be misled by the function name. What it really does is it returns bytes.
x2 = np.fromstring(x_bytes, dtype=x.dtype) # returns a 1-D array even if x is not.
print(np.array_equal(x, x2))


# Q6. Convert `a` into an ndarray and then convert it into a list again.

# In[9]:


a = [[1, 2], [3, 4]]
x = np.array(a)
a2 = x.tolist()
print(a == a2)


# ## String formatting¶

# Q7. Convert `x` to a string, and revert it.

# In[10]:


x = np.arange(10).reshape(2,5)
x_str = np.array_str(x)
print(x_str, "\n", type(x_str))
x_str = x_str.replace("[", "") # [] must be stripped
x_str = x_str.replace("]", "")
x2 = np.fromstring(x_str, dtype=x.dtype, sep=" ").reshape(x.shape)
assert np.array_equal(x, x2)


# ## Text formatting options

# Q8. Print `x` such that all elements are displayed with precision=1, no suppress.

# In[11]:


x = np.random.uniform(size=[10,100])
np.set_printoptions(precision=1, threshold=np.nan, suppress=True)
print(x)


# ## Base-n representations

# Q9. Convert 12 into a binary number in string format.

# In[12]:


out1 = np.binary_repr(12)
out2 = np.base_repr(12, base=2)
assert out1 == out2 # But out1 is better because it's much faster.
print(out1)


# Q10. Convert 12 into a hexadecimal number in string format.

# In[13]:


np.base_repr(1100, base=16)

