# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:09:52 2026

@author: Lenovo
"""

s = input("Enter a string: ")

count = 0
n = len(s)

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        count = count + 1

print("Changes needed:", count)