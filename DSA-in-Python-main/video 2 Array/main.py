
'''
line 50 = slicing concept
line 71 = dynamic array concept
line 92 = search value
line 107 = NUMPY
line 148 = Multidimensional Array
line 181 = complete or last line
# import array as arr # arr is alias name

from array import * # full array module is import in the file  (don't need to use method with alias name)

val = array('i',[1,2,3,4,5,6,7,8, 9]) # here directly array method can be used
# d is typecode for float

for i in range(0,len(val)):
    print(val[i], end=" ") # end = " " is called a keyword argument

print('\n')

for x in val: # enhanced for loop not need to give range here
    print(x , end = ' , ')

print('\n')

print(val.typecode)
i = int ,, d = float  ,, u = char
val.reverse() # feature is directly val array is reverse without store in another array

for x in val:
    print(x , end = ' , ')

print('\n')

val.insert(1,50) # element not delete only insert (list method) SYNTAX = (INDEX , VALUE).
val.append(100) # insert value in last.
val[2] = 300 # change value of 2nd index.

copyArray = array(val.typecode , [x * 3 for x in val]) # first loop then x store val values in each iteration
'''
#copyArray.pop() # remove index 3 || if not give INDEX then last index delete.

copyArray.remove(15) # here give value

# .pop use to delete when index know or delete last value and .remove used when value is known
'''
for x in copyArray:
    print(x , end = ' , ')

    # bookmark 31

'''


#### slicing concept
'''
from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

# abc = val[2 : 5] # slicing [start index : end index] // **include last index value or not? => not include

# abc = val[2 : -3] # -3 means not include last 3 index, means value 7 , 8 and 9 not include 

abc = val[::-1]# reverse value daal degi val array ki because [start : stop : step] here value backward jayegi last element se first element tak

# not include last index in both range and slicing

for i in range(len(abc)):
    print(abc[i] , end = " , ")

'''


### dynamic array concept
""" 
from array import *

arr = array('i',{})

n = int(input("Enter how many element you wnat to enter: ")) # or enter size of the array

for i in range(n):
    # k = int(input(f"Enter value of arr[{i}]: "))
    arr.append(int(input(f"Enter value of arr[{i}]: "))) # this also word not need another variable

for l in arr:
    print(l , end = " ") # end used to seperate value or add something after print value

# time complexity = 0(n)
# space complexity = 0(n)
 """


# search value
""" 
from array import *

arr = array("i" , [12,343,53,100,300])

i = arr.index(343)

print(i)
 """

# ____________________________

# NUMPY LIBRARAY
'''

# import numpy as np
from numpy import *

# val = array([12,3,43,5,3.6]) # here not need to write typecode

# val = array([1 , 3 ,5] , float) # here we also add typecode

# val = linspace(10 , 20 , 11) #** (start , end , partition in how many parts)
# means 10 se 20 number tak 11 partition kar dega
# linspace partition in equal distance
# also include both start and end value


# val = arange(10 , 20 , 6) # (start , end , comman difference)
# same like linspace but have comman difference and not include end parameter value
# inlcude start value but not end value

# for x in val:
#     print(x , end = " ")

# print(type(val[1]))
# Numpy benefit is it make array of heterogenous(different values) elements
# * float value bhi insert karege to sari value float mein convert ho jayegi
# * char value insert karne se sari value character mein badal jayegi.

# val = zeros(10) #  In val array all elements are 0 value and number of array size is 10
# val = ones(10) # same like zeros
# used when to store all zero value in array or one value

val = full(12 , 3) # SYNTAX => (SIZE , VALUE)
# used when to store same value in every element

for x in val:
    print(x , end = " ")

'''


# Multidimensional Array

from numpy import *
'''
zero = array(10)
print(zero)

one = array([1,2,3,4,5])
print(one)
// [] square bracket , {curly braces} , ; semicolon , : colon , , comman , " " quotition mark 
two = array([[1,2,3] , [4,5,6] , [7,8,9]]) // first is outer square bracket
print(two)
# two dimensional array is collection of 1 dimensional array
# dimension matlab direction or level

one = array([1,23,4])
two = ([ [1,23 ,4] ])
# The outer brackets represent the collection of rows, while the inner brackets represent individual rows in a 2D array.

# Outer list → rows ka container

# Inner list → ek row ka data
three = array([ [[1,2,3] , [4,5,6]] , [[5,6,7], [7,8,9]] ])# first bracket is outer bracket
print(three)
# three dimensional array is the collection of two dimensional array
# one = array([1,2,3])

four = array([ [ [ [ 1 ,2 ] ] , [ [1 ,2] ] ] , [ [ [1, 2]] , [ [1 ,2] ]  ]])
print(four)
# outer bracket represent conainer for rows

'''
# complete array of python



