# coding: utf-8
import numpy as np
x = [1,2]
y = [[4, 1], [2, 2]]
#print np.dot(x, y)
#print np.dot(y, x)
#print np.matmul(x, y)
#print np.inner(x, y)
#print np.inner(y, x)


# Q2. Predict the results of the following code.

# In[52]:


x = [[1, 0], [0, 1]]
y = [[4, 1], [2, 2], [1, 1]]
#print np.dot(y, x)
#print np.matmul(y, x)


# Q3. Predict the results of the following code.

# In[37]:


x = np.array([[1, 4], [5, 6]])
y = np.array([[4, 1], [2, 2]])
#print np.vdot(x, y)
#print np.vdot(y, x)
#print np.dot(x.flatten(), y.flatten())
#print np.inner(x.flatten(), y.flatten())
#print (x*y).sum()


# Q4. Predict the results of the following code.

# In[45]:


x = np.array(['a', 'b'], dtype=object)
y = np.array([1, 2])
#print np.inner(x, y)
#print np.inner(y, x)
#print np.outer(x, y)
#print np.outer(y, x)


# ## Decompositions

# Q5. Get the lower-trianglular `L` in the Cholesky decomposition of x and verify it.

# In[97]:


x = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=np.int32)


# Q6. Compute the qr factorization of x and verify it.

# In[107]:


x = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=np.float32)


# Q7. Factor x by Singular Value Decomposition and verify it.

# In[165]:


x = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float32)


# ## Matrix eigenvalues

# Q8. Compute the eigenvalues and right eigenvectors of x. (Name them eigenvals and eigenvecs, respectively)

# In[77]:


x = np.diag((1, 2, 3))


# Q9. Predict the results of the following code.

# In[81]:


#print np.array_equal(np.dot(x, eigenvecs), eigenvals * eigenvecs)


# ## Norms and other numbers

# Q10. Calculate the Frobenius norm and the condition number of x.

# In[12]:


x = np.arange(1, 10).reshape((3, 3))


# Q11. Calculate the determinant of x.

# In[22]:


x = np.arange(1, 5).reshape((2, 2))


# Q12. Calculate the rank of x.

# In[35]:


x = np.eye(4)


# Q13. Compute the sign and natural logarithm of the determinant of x.

# In[49]:


x = np.arange(1, 5).reshape((2, 2))


# Q14. Return the sum along the diagonal of x.

# In[57]:


x = np.eye(4)


# ## Solving equations and inverting matrices

# Q15. Compute the inverse of x.

# In[60]:


x = np.array([[1., 2.], [3., 4.]])

