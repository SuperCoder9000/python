# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:08:22 2024

@author: KIIT0001
"""

weight = float(input("Whats your weight? "))
unit = input("(L)bs or (K)gs? ")
if unit.upper() == "L":
    conv = weight*0.45
    print(f"your weight is {conv} kilos")
else:
    conv = weight/0.45
    print(f"your weight is {conv} pounds")