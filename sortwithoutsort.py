#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:17:28 2023

@author: hkashmiri23
"""
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 13, 16, 17, 18, 10]
def selSort(nums):
    n = len(nums)
# len helps you count how many things are in a list
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if nums[i] < nums[mp]:
                mp = i
            nums[bottom], nums[mp] = nums[mp], nums[bottom]

import random
l1=[random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)] 
print("Original List:", l1)
 
# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
# sorted list
print("Sorted List", l1)

for i in range(n - 1):
    if i == b:
        print('yes')
    else:
        print('no')