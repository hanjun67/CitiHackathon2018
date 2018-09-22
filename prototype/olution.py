# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:04:42 2018

@author: Asus
"""

def solution(indices, K):
    length = len(indices)
    arr = []
    if length % K != 0:
        min_size = length // K
        remainder = length % K
    first = 0
    last = min_size
    maxed = False
    for i in range(K):
        if remainder > 0:
            last += 1
            remainder -= 1
            maxed = True
        arr.append(indices[:first] + indices[last:])
        arr.append(indices[first:last])
        if maxed == True:
            first += min_size + 1
            maxed = False
        else:
            first += min_size
        last += min_size
    return arr
    pass