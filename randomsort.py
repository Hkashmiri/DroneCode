#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:32:59 2023

@author: hkashmiri23
"""
import random

def genrandnumers(lowest, highest, length):
    listOfNumbers = []
    for i in range(length):
        x = random.randint(lowest, highest)
        listOfNumbers.append(x)
        
    return listOfNumbers


def bubbleSort(elements):
    n = len(elements)
    swapped = True
    counter = 0
    
    while (swapped == True):
        swapped = False
        for i in range(n-1):
            counter += 1
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True
    return elements, counter

def selectionSort(elements):
   counter = 0
   for i in range(0, len(elements)):
       for x in range(0, len(elements)):
           counter += 1
           if(elements[i] < elements[x]):
               elements[i], elements[x] = elements[x], elements[i]
   return elements, counter

newList = genrandnumers(-1000, 1000, random.randint(-50, 50))
print(newList)
print(bubbleSort(newList))
print(selectionSort(newList))