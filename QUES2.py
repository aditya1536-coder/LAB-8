# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:04:56 2026

@author: Lenovo
"""

s = input("Enter a string: ")

result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result = result + s[i].upper()
    else:
        result = result + s[i].lower()

print(result)