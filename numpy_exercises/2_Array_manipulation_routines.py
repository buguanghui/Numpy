
# coding: utf-8

# # Array manipulation routines

# In[1]:


import numpy as np


# In[2]:


np.__version__


# Q1. Let x be a ndarray [10, 10, 3] with all elements set to one. Reshape x so that the size of the second dimension equals 150.

# In[5]:





# Q2. Let x be array [[1, 2, 3], [4, 5, 6]]. Convert it to [1 4 2 5 3 6].

# In[22]:





# Q3. Let x be array [[1, 2, 3], [4, 5, 6]]. Get the 5th element.

# In[23]:





# Q4. Let x be an arbitrary 3-D array of shape (3, 4, 5). Permute the dimensions of x such that the new shape will be (4,3,5).
# 

# In[36]:





# Q5. Let x be an arbitrary 2-D array of shape (3, 4). Permute the dimensions of x such that the new shape will be (4,3).

# In[38]:





# Q5. Let x be an arbitrary 2-D array of shape (3, 4). Insert a nex axis such that the new shape will be (3, 1, 4).

# In[42]:





# Q6. Let x be an arbitrary 3-D array of shape (3, 4, 1). Remove a single-dimensional entries such that the new shape will be (3, 4).

# In[43]:





# Q7. Lex x be an array <br/>
# [[ 1 2 3]<br/>
# [ 4 5 6].<br/><br/>
# and y be an array <br/>
# [[ 7 8 9]<br/>
# [10 11 12]].<br/>
# Concatenate x and y so that a new array looks like <br/>[[1, 2, 3, 7, 8, 9], <br/>[4, 5, 6, 10, 11, 12]].
# 

# In[31]:





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





# Q8. Let x be an array [1 2 3] and y be [4 5 6]. Convert it to [[1, 4], [2, 5], [3, 6]].

# In[54]:





# Q9. Let x be an array [[1],[2],[3]] and y be [[4], [5], [6]]. Convert x to [[[1, 4]], [[2, 5]], [[3, 6]]].

# In[34]:





# Q10. Let x be an array [1, 2, 3, ..., 9]. Split x into 3 arrays, each of which has 4, 2, and 3 elements in the original order.

# In[62]:





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





# Q12. Let x be an array <br />
# [[  0.,   1.,   2.,   3.],<br>
#  [  4.,   5.,   6.,   7.],<br>
#  [  8.,   9.,  10.,  11.],<br>
#  [ 12.,  13.,  14.,  15.]].<br>
# Split it into two arrays along the second axis.

# In[74]:





# Q13. Let x be an array <br />
# [[  0.,   1.,   2.,   3.],<br>
#  [  4.,   5.,   6.,   7.],<br>
#  [  8.,   9.,  10.,  11.],<br>
#  [ 12.,  13.,  14.,  15.]].<br>
# Split it into two arrays along the first axis.

# In[75]:





# Q14. Let x be an array [0, 1, 2]. Convert it to <br/>
# [[0, 1, 2, 0, 1, 2],<br/>
#  [0, 1, 2, 0, 1, 2]].

# In[93]:





# Q15. Let x be an array [0, 1, 2]. Convert it to <br/>
# [0, 0, 1, 1, 2, 2].

# In[83]:





# Q16. Let x be an array [0, 0, 0, 1, 2, 3, 0, 2, 1, 0].<br/>
# remove the leading the trailing zeros.

# In[105]:





# Q17. Let x be an array [2, 2, 1, 5, 4, 5, 1, 2, 3]. Get two arrays of unique elements and their counts.
# 

# In[107]:





# Q18. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Flip x along the second axis.

# In[120]:





# Q19. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Flip x along the first axis.

# In[121]:





# Q20. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Rotate x 90 degrees counter-clockwise.

# In[122]:





# Q21 Lex x be an array <br/>
# [[ 1 2 3 4]<br/>
#  [ 5 6 7 8].<br/>
# Shift elements one step to right along the second axis.

# In[126]:




