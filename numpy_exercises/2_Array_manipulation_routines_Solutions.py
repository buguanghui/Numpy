
# coding: utf-8

# # Array manipulation routines

# In[1]:


import numpy as np


# In[2]:


np.__version__


# Q1. Let x be a ndarray [10, 10, 3] with all elements set to one. Reshape x so that the size of the second dimension equals 150.

# In[5]:


x = np.ones([10, 10, 3])
out = np.reshape(x, [-1, 150])
print out
assert np.allclose(out, np.ones([10, 10, 3]).reshape([-1, 150]))


# Q2. Let x be array [[1, 2, 3], [4, 5, 6]]. Convert it to [1 4 2 5 3 6].

# In[22]:


x = np.array([[1, 2, 3], [4, 5, 6]])
out1 = np.ravel(x, order='F')
out2 = x.flatten(order="F")
assert np.allclose(out1, out2)
print out1


# Q3. Let x be array [[1, 2, 3], [4, 5, 6]]. Get the 5th element.

# In[23]:


x = np.array([[1, 2, 3], [4, 5, 6]])
out1 = x.flat[4]
out2 = np.ravel(x)[4]
assert np.allclose(out1, out2)
print out1


# Q4. Let x be an arbitrary 3-D array of shape (3, 4, 5). Permute the dimensions of x such that the new shape will be (4,3,5).
# 

# In[36]:


x = np.zeros((3, 4, 5))
out1 = np.swapaxes(x, 1, 0)
out2 = x.transpose([1, 0, 2])
assert out1.shape == out2.shape
print out1.shape


# Q5. Let x be an arbitrary 2-D array of shape (3, 4). Permute the dimensions of x such that the new shape will be (4,3).

# In[38]:


x = np.zeros((3, 4))
out1 = np.swapaxes(x, 1, 0)
out2 = x.transpose()
out3 = x.T
assert out1.shape == out2.shape == out3.shape
print out1.shape


# Q5. Let x be an arbitrary 2-D array of shape (3, 4). Insert a nex axis such that the new shape will be (3, 1, 4).

# In[42]:


x = np.zeros((3, 4))
print np.expand_dims(x, axis=1).shape


# Q6. Let x be an arbitrary 3-D array of shape (3, 4, 1). Remove a single-dimensional entries such that the new shape will be (3, 4).

# In[43]:


x = np.zeros((3, 4, 1))
print np.squeeze(x).shape


# Q7. Lex x be an array <br/>
# [[ 1 2 3]<br/>
# [ 4 5 6].<br/><br/>
# and y be an array <br/>
# [[ 7 8 9]<br/>
# [10 11 12]].<br/>
# Concatenate x and y so that a new array looks like <br/>[[1, 2, 3, 7, 8, 9], <br/>[4, 5, 6, 10, 11, 12]].
# 

# In[31]:


x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
out1 = np.concatenate((x, y), 1)
out2 = np.hstack((x, y))
assert np.allclose(out1, out2)
print out2


# Q8. Lex x be an array <br/>
# [[ 1 2 3]<br/>
# [ 4 5 6].<br/><br/>
# and y be an array <br/>
# [[ 7 8 9]<br/>
# [10 11 12]].<br/>
# Concatenate x and y so that a new array looks like <br/>[[ 1  2  3]<br/>
#  [ 4  5  6]<br/>
#  [ 7  8  9]<br/>
#  [10 11 12]]
# 

# In[38]:


x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
out1 = np.concatenate((x, y), 0)
out2 = np.vstack((x, y))
assert np.allclose(out1, out2)
print out2


# Q8. Let x be an array [1 2 3] and y be [4 5 6]. Convert it to [[1, 4], [2, 5], [3, 6]].

# In[9]:


x = np.array((1,2,3))
y = np.array((4,5,6))
out1 = np.column_stack((x, y))
out2 = np.squeeze(np.dstack((x, y)))
out3 = np.vstack((x, y)).T
assert np.allclose(out1, out2)
assert np.allclose(out2, out3)
print out1


# Q9. Let x be an array [[1],[2],[3]] and y be [[4], [5], [6]]. Convert x to [[[1, 4]], [[2, 5]], [[3, 6]]].

# In[34]:


x = np.array([[1],[2],[3]])
y = np.array([[4],[5],[6]])
out = np.dstack((x, y))
print out


# Q10. Let x be an array [1, 2, 3, ..., 9]. Split x into 3 arrays, each of which has 4, 2, and 3 elements in the original order.

# In[62]:


x = np.arange(1, 10)
print np.split(x, [4, 6])


# Q11. Let x be an array<br/>
# [[[  0.,   1.,   2.,   3.],<br/>
#   [  4.,   5.,   6.,   7.]],<br/>
#  
#  [[  8.,   9.,  10.,  11.],<br/>
#   [ 12.,  13.,  14.,  15.]]].<br/>
# Split it into two such that the first array looks like<br/>
# [[[  0.,   1.,   2.],<br/>
#   [  4.,   5.,   6.]],<br/>
#  
#  [[  8.,   9.,  10.],<br/>
#   [ 12.,  13.,  14.]]].<br/>
#   
# and the second one look like:<br/>
#   
# [[[  3.],<br/>
#   [  7.]],<br/>
#  
#  [[  11.],<br/>
#   [ 15.]]].<br/>  

# In[72]:


x = np.arange(16).reshape(2, 2, 4)
out1 = np.split(x, [3],axis=2)
out2 = np.dsplit(x, [3])
assert np.allclose(out1[0], out2[0])
assert np.allclose(out1[1], out2[1])
print out1


# Q12. Let x be an array <br />
# [[  0.,   1.,   2.,   3.],<br>
#  [  4.,   5.,   6.,   7.],<br>
#  [  8.,   9.,  10.,  11.],<br>
#  [ 12.,  13.,  14.,  15.]].<br>
# Split it into two arrays along the second axis.

# In[74]:


x = np.arange(16).reshape((4, 4))
out1 = np.hsplit(x, 2)
out2 = np.split(x, 2, 1)
assert np.allclose(out1[0], out2[0])
assert np.allclose(out1[1], out2[1])
print out1


# Q13. Let x be an array <br />
# [[  0.,   1.,   2.,   3.],<br>
#  [  4.,   5.,   6.,   7.],<br>
#  [  8.,   9.,  10.,  11.],<br>
#  [ 12.,  13.,  14.,  15.]].<br>
# Split it into two arrays along the first axis.

# In[75]:


x = np.arange(16).reshape((4, 4))
out1 = np.vsplit(x, 2)
out2 = np.split(x, 2, 0)
assert np.allclose(out1[0], out2[0])
assert np.allclose(out1[1], out2[1])
print out1


# Q14. Let x be an array [0, 1, 2]. Convert it to <br/>
# [[0, 1, 2, 0, 1, 2],<br/>
#  [0, 1, 2, 0, 1, 2]].

# In[93]:


x = np.array([0, 1, 2])
out1 = np.tile(x, [2, 2])
out2 = np.resize(x, [2, 6])
assert np.allclose(out1, out2)
print out1


# Q15. Let x be an array [0, 1, 2]. Convert it to <br/>
# [0, 0, 1, 1, 2, 2].

# In[83]:


x = np.array([0, 1, 2])
print np.repeat(x, 2)


# Q16. Let x be an array [0, 0, 0, 1, 2, 3, 0, 2, 1, 0].<br/>
# remove the leading the trailing zeros.

# In[105]:


x = np.array((0, 0, 0, 1, 2, 3, 0, 2, 1, 0))
out = np.trim_zeros(x)
print out


# Q17. Let x be an array [2, 2, 1, 5, 4, 5, 1, 2, 3]. Get two arrays of unique elements and their counts.
# 

# In[107]:


x = np.array([2, 2, 1, 5, 4, 5, 1, 2, 3])
u, indices = np.unique(x, return_counts=True)
print u, indices


# Q18. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Flip x along the second axis.

# In[120]:


x = np.array([[1,2], [3,4]])
out1 = np.fliplr(x)
out2 = x[:, ::-1]
assert np.allclose(out1, out2)
print out1


# Q19. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Flip x along the first axis.

# In[121]:


x = np.array([[1,2], [3,4]])
out1 = np.flipud(x)
out2 = x[::-1, :]
assert np.allclose(out1, out2)
print out1


# Q20. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Rotate x 90 degrees counter-clockwise.

# In[122]:


x = np.array([[1,2], [3,4]])
out = np.rot90(x)
print out


# Q21 Lex x be an array <br/>
# [[ 1 2 3 4]<br/>
#  [ 5 6 7 8].<br/>
# Shift elements one step to right along the second axis.

# In[126]:


x = np.arange(1, 9).reshape([2, 4])
print np.roll(x, 1, axis=1)

