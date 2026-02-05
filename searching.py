#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:26:55 2023

@author: hkashmiri23
"""

import random

def genrandnumers(lowest, highest, length):
    listOfNumbers = []
    for i in range(length):
        x = random.randint(lowest, highest)
        listOfNumbers.append(x)
        
    return listOfNumbers

# linear searching
def search(x, nums):
    counter = 0
    for i in range(len(nums)):
        counter += 1
        if nums[i] == x:
            return i 
    return -1, counter
#binary searching elements must be sorted for this to work
def searching(x,nums):
    counter = 0
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        item = nums[mid]
        counter +=1
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1, counter

newList = genrandnumers(-1000, 1000, random.randint(-50, 50))
print(newList)
print(search(1000, newList))
print(searching(1000, newList))
