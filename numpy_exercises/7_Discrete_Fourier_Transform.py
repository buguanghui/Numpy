
# coding: utf-8

# In[1]:


from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from datetime import date
date.today()

a = 1+1j
output = ...
print(output)


# Q2. Return the real part and imaginary part of `a`.

# In[6]:


a = np.array([1+2j, 3+4j, 5+6j])
real = ...
imag = ...
print("real part=", real)
print("imaginary part=", imag)


# Q3. Replace the real part of a with `9`, the imaginary part with `[5, 7, 9]`.

# In[7]:


a = np.array([1+2j, 3+4j, 5+6j])


print(a)


# Q4. Return the complex conjugate of `a`.

# In[8]:


a = 1+2j
output = ...
print(output)


# ### Discrete Fourier Transform

# Q5. Compuete the one-dimensional DFT of `a`.

# In[9]:


a = np.exp(2j * np.pi * np.arange(8))
output = ...
print(output)


# Q6. Compute the one-dimensional inverse DFT of the `output` in the above question.

# In[10]:


print("a=", a)
inversed = ...
print("inversed=", a)


# Q7. Compute the one-dimensional discrete Fourier Transform for real input `a`.

# In[11]:


a = [0, 1, 0, 0]
output = ...
print(output)
assert output.size==len(a)//2+1 if len(a)%2==0 else (len(a)+1)//2

# cf.
output2 = np.fft.fft(a)
print(output2)


# Q8. Compute the one-dimensional inverse DFT of the output in the above question.

# In[12]:


inversed = ...
print("inversed=", a)


# Q9. Return the DFT sample frequencies of `a`.

# In[13]:


signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=np.float32)
fourier = np.fft.fft(signal)
n = signal.size
freq = ...
print(freq)


# ### Window Functions

# In[14]:


fig = plt.figure(figsize=(19, 10))

# Hamming window
window = np.hamming(51)
plt.plot(np.bartlett(51), label="Bartlett window")
plt.plot(np.blackman(51), label="Blackman window")
plt.plot(np.hamming(51), label="Hamming window")
plt.plot(np.hanning(51), label="Hanning window")
plt.plot(np.kaiser(51, 14), label="Kaiser window")
plt.xlabel("sample")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

plt.show()

