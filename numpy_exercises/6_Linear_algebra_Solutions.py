
# coding: utf-8
import numpy as np
x = [1,2]
y = [[4, 1], [2, 2]]
print np.dot(x, y)
print np.dot(y, x)
print np.matmul(x, y)
print np.inner(x, y)
print np.inner(y, x)


# Q2. Predict the results of the following code.

# In[62]:


x = [[1, 0], [0, 1]]
y = [[4, 1], [2, 2], [1, 1]]
print np.dot(y, x)
print np.matmul(y, x)


# Q3. Predict the results of the following code.

# In[63]:


x = np.array([[1, 4], [5, 6]])
y = np.array([[4, 1], [2, 2]])
print np.vdot(x, y)
print np.vdot(y, x)
print np.dot(x.flatten(), y.flatten())
print np.inner(x.flatten(), y.flatten())
print (x*y).sum()


# Q4. Predict the results of the following code.

# In[65]:


x = np.array(['a', 'b'], dtype=object)
y = np.array([1, 2])
print np.inner(x, y)
print np.inner(y, x)
print np.outer(x, y)
print np.outer(y, x)


# ## Decompositions

# Q5. Get the lower-trianglular `L` in the Cholesky decomposition of x and verify it.

# In[97]:


x = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=np.int32)
L = np.linalg.cholesky(x)
print L
assert np.array_equal(np.dot(L, L.T.conjugate()), x)


# Q6. Compute the qr factorization of x and verify it.

# In[107]:


x = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=np.float32)
q, r = np.linalg.qr(x)
print "q=\n", q, "\nr=\n", r
assert np.allclose(np.dot(q, r), x)


# Q7. Factor x by Singular Value Decomposition and verify it.

# In[165]:


x = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float32)
U, s, V = np.linalg.svd(x, full_matrices=False)
print "U=\n", U, "\ns=\n", s, "\nV=\n", v
assert np.allclose(np.dot(U, np.dot(np.diag(s), V)), x)


# ## Matrix eigenvalues

# Q8. Compute the eigenvalues and right eigenvectors of x. (Name them eigenvals and eigenvecs, respectively)

# In[68]:


x = np.diag((1, 2, 3))
eigenvals = np.linalg.eig(x)[0]
eigenvals_ = np.linalg.eigvals(x)
assert np.array_equal(eigenvals, eigenvals_)
print "eigenvalues are\n", eigenvals
eigenvecs = np.linalg.eig(x)[1]
print "eigenvectors are\n", eigenvecs


# Q9. Predict the results of the following code.

# In[69]:


print np.array_equal(np.dot(x, eigenvecs), eigenvals * eigenvecs)


# ## Norms and other numbers

# Q10. Calculate the Frobenius norm and the condition number of x.

# In[12]:


x = np.arange(1, 10).reshape((3, 3))
print np.linalg.norm(x, 'fro')
print np.linalg.cond(x, 'fro')


# Q11. Calculate the determinant of x.

# In[22]:


x = np.arange(1, 5).reshape((2, 2))
out1 = np.linalg.det(x)
out2 = x[0, 0] * x[1, 1] - x[0, 1] * x[1, 0]
assert np.allclose(out1, out2)
print out1


# Q12. Calculate the rank of x.

# In[35]:


x = np.eye(4)
out1 = np.linalg.matrix_rank(x)
out2 = np.linalg.svd(x)[1].size
assert out1 == out2
print out1


# Q13. Compute the sign and natural logarithm of the determinant of x.

# In[49]:


x = np.arange(1, 5).reshape((2, 2))
sign, logdet = np.linalg.slogdet(x)
det = np.linalg.det(x)
assert sign == np.sign(det)
assert logdet == np.log(np.abs(det))
print sign, logdet


# Q14. Return the sum along the diagonal of x.

# In[57]:


x = np.eye(4)
out1 = np.trace(x)
out2 = x.diagonal().sum()
assert out1 == out2
print out1


# ## Solving equations and inverting matrices

# Q15. Compute the inverse of x.

# In[60]:


x = np.array([[1., 2.], [3., 4.]])
out1 = np.linalg.inv(x)
assert np.allclose(np.dot(x, out1), np.eye(2))
print out1

