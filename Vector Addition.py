# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Addition of Vectors 

import numpy as np

#A = np.array([(2),(-3), (7)])

#B = np.array([(5), (1), (2)])

while True: 
    try: 
        x = int(input("Enter x component of vector:")) 
    except ValueError: 
        print ("That is not an accepted value.")
    else: 
        break 
        
while True: 
    try: 
        y = int(input("Enter y component of vector:"))
    except ValueError: 
        print ("That is not an accepted value.")
    else: 
        break 
    
while True: 
    try: 
        z = int(input("Enter z component of vector:"))
    except ValueError: 
        print ("That is not an accepted value.")
    else: 
        break 

A = np.array([(x), (y), (z)])

while True: 
    try: 
        x2 = int(input("Enter x component of second vector:"))
    except ValueError: 
        print("That is not an accepted value.")
    else: 
        break 
while True: 
    try: 
        y2 = int(input("Enter y component of second vector:"))
    except ValueError: 
        print ("That is not an accepted value.")
    else: 
        break 

while True:    
    try: 
        z2 = int(input("Enter z component of second vector:"))
    except ValueError: 
        print("That is not an accepted value.")
    else: 
        break 

B = np.array([(x2), (y2), (z2)])

print ("The addition of the two vectors is", A+B, ".")
