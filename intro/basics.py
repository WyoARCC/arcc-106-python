#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Introduction to Python for Scientific Computing
October 17th, 2016
Advanced Research Computing Center
University of Wyoming

To be used with the Spyder Python 

"""

#%% How use libraries (more on this later)
import sys

#%% Basic Printing to "STDOUT"
print("Introduction to Python")

# More Direct Methods Notice the requirement of "\n"
sys.stdout.write("Welcome to ARCC!\n")

# Need to print to STDERR?
sys.stderr.write("This is where you should put WARNINGS / ERRORS.\n")

# May need to flush output buffers so be aware.
sys.stdout.flush()
sys.stderr.flush()

#%% Variable Types

# Strings (string of characters)
a_string = "string"

# Integers
a_integer = 1

# Floating Point
a_float = 2.0

# Complex Numbers (two part float: real and imaginary)
a_complex = 1+2j

# Real part of complex
rl = a_complex.real

# Imaginary part of complex
im = a_complex.imag

#%% Logical Checks

# In Python, boolean logic has both "True", and "False"

a_true_bool = True
a_false_bool = False

# If Statements
if a_true_bool:
    print(a_true_bool)

if not a_false_bool:
    print(a_false_bool)

if True == a_true_bool:
    print(a_true_bool)

if False == a_false_bool:
    print(a_false_bool)    

if a_false_bool:
    print("NO PRINTING HERE")
else:
    print("Printing here is good!")
    
#%% Containers

# A tuple, immutable like array
# Containers support different modes of access.
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a_tuple)          # Print container
print(a_tuple[0:3])     # Print first 4 elements, Python is 0-indexed
print(a_tuple[:-1])     # Print all except last value
print(a_tuple[::2])     # Print every other value
print(a_tuple[::-1])    # Print in reverse


# A list, mutable variable type array
# Can access in same methods as tuples
a_list = ["START",1, 2, 3, 4, 5, 6, 7, 8, 9, "DONE"]
print(a_list)

# A dictionary (associative array, hashtable)
# WARNING: ordering is arbitrary.
a_dictionary = {"one":1, "two": 2, "three":3}
print(a_dictionary)
print(a_dictionary["one"])

# A set, mutable container for math like sets. Create from list or iterable
# Sets are full of only unique values
a_set = set([1, 1, 2, 2, 3, 3, 4, 4])
print(a_set)


#%% Looping Methods
# Loops can be applied to containers.
# For: fixed iteration
for i in range(5):
    print(i)
    
for i in range(5,10):
    print(i)
    
for i in reversed(range(10)):
    print(i)
    
for i in a_list:
    print(i)

# While: logical iteration
i = 0
while (i < 10):
    print(i)
    i+=1

i = 0
a_new_list = []
while (i < 10):
    a_new_list.append(i)
    print(a_new_list)
    i += 1
    
while (a_new_list):
    a_new_list.pop()
    print(a_new_list)

i = 0
while (i < 10):
    a_new_list.insert(0,i)
    print(a_new_list)
    i += 1
    
# Dictionaries and Loops
for key in a_dictionary.keys():
    print(key,a_dictionary[key])

for key,value in a_dictionary.items():
    print(key,value)

# Sort dictionary by keys.
for key,value in sorted(a_dictionary.items()):
    print(key,value)
    
# Sort based on the value, not the key
# Here, we use a lambda function. These are probably more known
# as anonymous functions. We will see functions next.
for key,value in sorted(a_dictionary.items(),key=lambda value: value[1]):
    print(key,value)
    