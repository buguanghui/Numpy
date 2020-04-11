
# coding: utf-8

# # Mathematical functions

# In[1]:


import numpy as np


# In[2]:


np.__version__




x = np.array([0., 1., 30, 90])
print "sine:", np.sin(x)
print "cosine:", np.cos(x)
print "tangent:", np.tan(x)


# Q2. Calculate inverse sine, inverse cosine, and inverse tangent of x, element-wise.

# In[31]:


x = np.array([-1., 0, 1.])
print "inverse sine:", np.arcsin(x2)
print "inverse cosine:", np.arccos(x2)
print "inverse tangent:", np.arctan(x2)


# Q3. Convert angles from radians to degrees.

# In[45]:


x = np.array([-np.pi, -np.pi/2, np.pi/2, np.pi])

out1 = np.degrees(x)
out2 = np.rad2deg(x)
assert np.array_equiv(out1, out2)
print out1


# Q4. Convert angles from degrees to radians.

# In[48]:


x = np.array([-180.,  -90.,   90.,  180.])

out1 = np.radians(x)
out2 = np.deg2rad(x)
assert np.array_equiv(out1, out2)
print out1


# ## Hyperbolic functions

# Q5. Calculate hyperbolic sine, hyperbolic cosine, and hyperbolic tangent of x, element-wise.

# In[65]:


x = np.array([-1., 0, 1.])
print np.sinh(x)
print np.cosh(x)
print np.tanh(x)


# ## Rounding

# Q6. Predict the results of these, paying attention to the difference among the family functions.

# In[84]:


x = np.array([2.1, 1.5, 2.5, 2.9, -2.1, -2.5, -2.9])

out1 = np.around(x)
out2 = np.floor(x)
out3 = np.ceil(x)
out4 = np.trunc(x)
out5 = [round(elem) for elem in x]

print out1
print out2
print out3
print out4
print out5


# Q7. Implement out5 in the above question using numpy.

# In[87]:


print np.floor(np.abs(x) + 0.5) * np.sign(x) 
# Read http://numpy-discussion.10968.n7.nabble.com/why-numpy-round-get-a-different-result-from-python-round-function-td19098.html


# ## Sums, products, differences

# Q8. Predict the results of these.

# In[99]:


x = np.array(
    [[1, 2, 3, 4],
     [5, 6, 7, 8]])

outs = [np.sum(x),
        np.sum(x, axis=0),
        np.sum(x, axis=1, keepdims=True),
        "",
        np.prod(x),
        np.prod(x, axis=0),
        np.prod(x, axis=1, keepdims=True),
        "",
        np.cumsum(x),
        np.cumsum(x, axis=0),
        np.cumsum(x, axis=1),
        "",
        np.cumprod(x),
        np.cumprod(x, axis=0),
        np.cumprod(x, axis=1),
        "",
        np.min(x),
        np.min(x, axis=0),
        np.min(x, axis=1, keepdims=True),
        "",
        np.max(x),
        np.max(x, axis=0),
        np.max(x, axis=1, keepdims=True),
        "",
        np.mean(x),
        np.mean(x, axis=0),
        np.mean(x, axis=1, keepdims=True)]
           
for out in outs:
    if out == "":
        print
    else:
        print("->", out)


# Q9. Calculate the difference between neighboring elements, element-wise.

# In[100]:


x = np.array([1, 2, 4, 7, 0])
print np.diff(x)


# Q10. Calculate the difference between neighboring elements, element-wise, and
# prepend [0, 0] and append[100] to it.

# In[108]:


x = np.array([1, 2, 4, 7, 0])

out1 = np.ediff1d(x, to_begin=[0, 0], to_end=[100])
out2 = np.insert(np.append(np.diff(x), 100), 0, [0, 0])
assert np.array_equiv(out1, out2)
print out2


# Q11. Return the cross product of x and y.

# In[110]:


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print np.cross(x, y)


# ## Exponents and logarithms

# Q12. Compute $e^x$, element-wise.

# In[115]:


x = np.array([1., 2., 3.], np.float32)

out = np.exp(x)
print out


# Q13. Calculate exp(x) - 1 for all elements in x.

# In[118]:


x = np.array([1., 2., 3.], np.float32)

out1 = np.expm1(x)
out2 = np.exp(x) - 1.
assert np.allclose(out1, out2)
print out1


# Q14. Calculate $2^p$ for all p in x.

# In[124]:


x = np.array([1., 2., 3.], np.float32)

out1 = np.exp2(x)
out2 = 2 ** x
assert np.allclose(out1, out2)
print out1


# Q15. Compute natural, base 10, and base 2 logarithms of x element-wise.

# In[128]:


x = np.array([1, np.e, np.e**2])

print "natural log =", np.log(x)
print "common log =", np.log10(x)
print "base 2 log =", np.log2(x)


# Q16. Compute the natural logarithm of one plus each element in x in floating-point accuracy.

# In[131]:


x = np.array([1e-99, 1e-100])

print np.log1p(x)
# Compare it with np.log(1 +x)


# ## Floating point routines

# Q17. Return element-wise True where signbit is set.

# In[135]:


x = np.array([-3, -2, -1, 0, 1, 2, 3])

out1 = np.signbit(x)
out2 = x < 0
assert np.array_equiv(out1, out2)
print out1


# Q18. Change the sign of x to that of y, element-wise.

# In[140]:


x = np.array([-1, 0, 1])
y = -1.1

print np.copysign(x, y)


# ## Arithmetic operations

# Q19. Add x and y element-wise.

# In[141]:


x = np.array([1, 2, 3])
y = np.array([-1, -2, -3])

out1 = np.add(x, y)
out2 = x + y
assert np.array_equal(out1, out2)
print out1


# Q20. Subtract y from x element-wise.

# In[142]:


x = np.array([3, 4, 5])
y = np.array(3)

out1 = np.subtract(x, y)
out2 = x - y 
assert np.array_equal(out1, out2)
print out1


# Q21. Multiply x by y element-wise.

# In[144]:


x = np.array([3, 4, 5])
y = np.array([1, 0, -1])

out1 = np.multiply(x, y)
out2 = x * y 
assert np.array_equal(out1, out2)
print out1


# Q22. Divide x by y element-wise in two different ways.

# In[161]:


x = np.array([3., 4., 5.])
y = np.array([1., 2., 3.])

out1 = np.true_divide(x, y)
out2 = x / y 
assert np.array_equal(out1, out2)
print out1

out3 = np.floor_divide(x, y)
out4 = x // y
assert np.array_equal(out3, out4)
print out3

# Note that in Python 2 and 3, the handling of `divide` differs.
# See https://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html#numpy.divide


# Q23. Compute numerical negative value of x, element-wise.

# In[146]:


x = np.array([1, -1])

out1 = np.negative(x)
out2 = -x
assert np.array_equal(out1, out2)
print out1


# Q24. Compute the reciprocal of x, element-wise.

# In[155]:


x = np.array([1., 2., .2])

out1 = np.reciprocal(x)
out2 = 1/x
assert np.array_equal(out1, out2)
print out1


# Q25. Compute $x^y$, element-wise.

# In[163]:


x = np.array([[1, 2], [3, 4]])
y = np.array([[1, 2], [1, 2]])

out = np.power(x, y)
print out


# Q26. Compute the remainder of x / y element-wise in two different ways.

# In[168]:


x = np.array([-3, -2, -1, 1, 2, 3])
y = 2

out1 = np.mod(x, y)
out2 = x % y
assert np.array_equal(out1, out2)
print out1

out3 = np.fmod(x, y)
print out3


# ## Miscellaneous

# Q27. If an element of x is smaller than 3, replace it with 3.
# And if an element of x is bigger than 7, replace it with 7.

# In[174]:


x = np.arange(10)

out1 = np.clip(x, 3, 7)
out2 = np.copy(x)
out2[out2 < 3] = 3
out2[out2 > 7] = 7

assert np.array_equiv(out1, out2)
print out1


# Q28. Compute the square of x, element-wise.

# In[176]:


x = np.array([1, 2, -1])

out1 = np.square(x)
out2 = x * x
assert np.array_equal(out1, out2)
print out1


# Q29. Compute square root of x element-wise.
# 

# In[177]:


x = np.array([1., 4., 9.])

out = np.sqrt(x)
print out


# Q30. Compute the absolute value of x.

# In[178]:


x = np.array([[1, -1], [3, -3]])

out = np.abs(x)
print out


# Q31. Compute an element-wise indication of the sign of x, element-wise.

# In[181]:


x = np.array([1, 3, 0, -1, -3])

out1 = np.sign(x)
out2 = np.copy(x)
out2[out2 > 0] = 1
out2[out2 < 0] = -1
assert np.array_equal(out1, out2)
print out1

