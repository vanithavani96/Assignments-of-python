#!/usr/bin/env python
# coding: utf-8

# 1.write a program to print yourself introduction

# In[2]:


name="My name is vanitha"
qualification="UG"
gpa=7.62
skills="good communication skill and self learning skill"
strength="patience"
print(name)
print(qualification)
print(gpa)
print(skills)
print(strength)


# 2.write a program to perform the following operations
# *Addition
# *Subtraction
# *Multiplication
# *Division
# *Modulus
# *Exponent
# 

# In[3]:


a=2  #addition of two numbers
b=3
c=a+b
print("The sum is:",c)


# In[4]:


a=10 #subtraction
b=5
c=a-b
print("The difference is:",c)


# In[8]:


a=int(input("enter the number")) #Multiplication
b=int(input("enter the number"))
c=a*b
print("The product of two number is:",c)


# In[9]:


a=20 #Division
b=2
c=a/b
print("The result is:",c)


# In[11]:


a=30  #Modulus
b=7
c=a%b
print("The output is:",c)


# In[13]:


a=4  #Exponent
b=a**2
print("The result is:",b)


# 3.Wirte a program of swap two numbers.

# In[18]:


a=3
b=2
c=a
a=b
b=c
print("value of a after swapping is:", a)
print("value of b after swapping is:", b)


# 4.Write a program to swap two numbers without using third variable.

# In[19]:


x=5
y=10
print("the value of x before swapping is:",x)
print("the value of y before swapping is:",y)
x,y=y,x
print("The value of x after swapping is:", x)
print("The value of y after swapping is:", y)


# 5.Write a program to compute simple interest.

# In[21]:


p=1000
r=5
t=2
SI=(p*r*t)/100
print("the simple interest is:",SI)


# 6.Write a program to find average of five numbers by user input

# In[2]:


a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))
e=int(input("enter the number:"))
avg=(a+b+c+d+e)/5
print("The average is:", avg)


# 7.Write a program to calculate the discriminant of a quadratic equation.

# In[1]:


a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))
d=(b**2)-(4*a*c)
print("the solution is:", d)


# In[ ]:




