#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:10:32 2023

@author: hkashmiri23
"""

import random

def GeneralRandomListOfNumbers(length, lowest, highest):
    
    list_of_numbers = []
    for i in range(length):
        x = random.randint(lowest, highest)
        list_of_numbers.append(x)
    return list_of_numbers

def search(ListOfNumbers, nums):
    
    operation_counter = 0
    for i in range(len(nums)):
        if nums[i] == ListOfNumbers:
            operation_counter += 1
            return i, operation_counter
    return - 1, operation_counter

def searching(x,nums):
    
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return - 1