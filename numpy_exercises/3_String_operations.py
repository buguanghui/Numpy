# coding: utf-8

from __future__ import print_function
import numpy as np

np.__version__

x1 = np.array(['Hello', 'Say'], dtype=np.str)
x2 = np.array([' world', ' something'], dtype=np.str)


# Q2. Repeat x three time element-wise.

# In[5]:


x = np.array(['Hello ', 'Say '], dtype=np.str)


# Q3-1. Capitalize the first letter of x element-wise.<br/>
# Q3-2. Lowercase x element-wise.<br/>
# Q3-3. Uppercase x element-wise.<br/>
# Q3-4. Swapcase x element-wise.<br/>
# Q3-5. Title-case x element-wise.<br/>

# In[6]:


x = np.array(['heLLo woRLd', 'Say sOmething'], dtype=np.str)
capitalized = ...
lowered = ...
uppered = ...
swapcased = ...
titlecased = ...
print("capitalized =", capitalized)
print("lowered =", lowered)
print("uppered =", uppered)
print("swapcased =", swapcased)
print("titlecased =", titlecased)


# Q4. Make the length of each element 20 and the string centered / left-justified / right-justified with paddings of `_`.

# In[7]:


x = np.array(['hello world', 'say something'], dtype=np.str)
centered = ...
left = ...
right = ...

print("centered =", centered)
print("left =", left)
print("right =", right)


# Q5. Encode x in cp500 and decode it again.

# In[8]:


x = np.array(['hello world', 'say something'], dtype=np.str)
encoded = ...
decoded = ...
print("encoded =", encoded)
print("decoded =", decoded)


# Q6. Insert a space between characters of x.

# In[9]:


x = np.array(['hello world', 'say something'], dtype=np.str)


# Q7-1. Remove the leading and trailing whitespaces of x element-wise.<br/>
# Q7-2. Remove the leading whitespaces of x element-wise.<br/>
# Q7-3. Remove the trailing whitespaces of x element-wise.

# In[10]:


x = np.array(['   hello world   ', '\tsay something\n'], dtype=np.str)
stripped = ...
lstripped = ...
rstripped = ...
print("stripped =", stripped)
print("lstripped =", lstripped)
print("rstripped =", rstripped)


# Q8. Split the element of x with spaces.

# In[11]:


x = np.array(['Hello my name is John'], dtype=np.str)


# Q9. Split the element of x to multiple lines.

# In[12]:


x = np.array(['Hello\nmy name is John'], dtype=np.str)


# Q10. Make x a numeric string of 4 digits with zeros on its left.

# In[13]:


x = np.array(['34'], dtype=np.str)


# Q11. Replace "John" with "Jim" in x.

# In[14]:


x = np.array(['Hello nmy name is John'], dtype=np.str)


# ## Comparison

# Q12. Return x1 == x2, element-wise.

# In[15]:


x1 = np.array(['Hello', 'my', 'name', 'is', 'John'], dtype=np.str)
x2 = np.array(['Hello', 'my', 'name', 'is', 'Jim'], dtype=np.str)


# Q13. Return x1 != x2, element-wise.

# In[16]:


x1 = np.array(['Hello', 'my', 'name', 'is', 'John'], dtype=np.str)
x2 = np.array(['Hello', 'my', 'name', 'is', 'Jim'], dtype=np.str)


# ## String information

# Q14. Count the number of "l" in x, element-wise.

# In[17]:


x = np.array(['Hello', 'my', 'name', 'is', 'Lily'], dtype=np.str)


# Q15. Count the lowest index of "l" in x, element-wise.

# In[18]:


x = np.array(['Hello', 'my', 'name', 'is', 'Lily'], dtype=np.str)



# Q16-1. Check if each element of x is composed of digits only.<br/>
# Q16-2. Check if each element of x is composed of lower case letters only.<br/>
# Q16-3. Check if each element of x is composed of upper case letters only.

# In[19]:


x = np.array(['Hello', 'I', 'am', '20', 'years', 'old'], dtype=np.str)
out1 = ...
out2 = ...
out3 = ...
print("Digits only =", out1)
print("Lower cases only =", out2)
print("Upper cases only =", out3)


# Q17. Check if each element of x starts with "hi".

# In[20]:


x = np.array(['he', 'his', 'him', 'his'], dtype=np.str)

