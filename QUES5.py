# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:06:55 2026

@author: Lenovo
"""

s = input("Enter a sentence: ")

words = s.split()

for word in words:
    print(len(word), end=" ")