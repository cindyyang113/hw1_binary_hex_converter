#!/usr/bin/env python
# coding: utf-8

# 2進位轉換成16進位:
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


# 10進位轉換成16進位:
# Conversion table of remainders to hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
 
 
# function which converts decimal value to hexadecimal value
decimal = int(input("Enter a decimal number \n"))
def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
 
    return hexadecimal
 
 
print("The hexadecimal form of", decimal,
      "is", decimalToHexadecimal(decimal))
