#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:10:55 2023

@author: hkashmiri23
"""
while(low<=high):
    mid = (low + high) // 2
    operation_counter += 1
    if NumberToFind == ListOfNumbers[mid]:
        return mid, operation_counter
    elif NumberToFind < ListOfNumbers[mid]:
        high = mid - 1
    elif NumberToFind > ListOfNumbers[mid]:
        high = mid + 1
return -1, operation_counter


def RunSearchExperiment (N,length,lowest,highest):
    for exp in range(N):
        test_list = GenerateRandomListOfNumbers(length,lowest,highest)
        test_list.sort()
        print(test_number)
        
        found_loc, ops = LinearSearch(test_list,test_number)
        print(Linear Search -- Found at location %s using %s operations)
        
        found_loc, ops = BinarySearch(test_list,test_number)
        print(Binary Search -- Found at location %s using %s operations)