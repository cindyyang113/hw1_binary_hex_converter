#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get input and initialize variables
decimal = int(input("Enter a decimal number \n"))
binary = 0
ctr = 0
temp = decimal  #copy input decimal

#find binary value using while loop
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary  #取餘數並乘於次數
    temp = int(temp/2)   #將被除數除二
    ctr += 1   #將次數加一

#output the result       
print("Binary of {x} is: {y}".format(x=decimal,y=binary))


# In[14]:


decimal = int(input("Enter a decimal number \n"))
answer = hex(decimal)
answer = (answer[2:])
print("Hexadecimal of {x} is: {y}".format(x=decimal,y=answer))

