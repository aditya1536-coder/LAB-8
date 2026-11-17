# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:10:03 2026

@author: Lenovo
"""

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print(result)