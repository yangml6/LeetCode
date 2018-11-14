#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:54:59 2018

@author: yml
"""

#第一、最后可视为前后各加一个0
import re
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        return sum(map(lambda x:(len(x)-1)//2, ('0'+''.join(map(str, flowerbed))+'0').split('1'))) >= n


    def canPlaceFlowers2(self, flowerbed, n):
        have = [-2] + [i for i, x in enumerate(flowerbed) if x] + [len(flowerbed) + 1]
        return sum(abs(have[i] - have[i-1] - 2) // 2 for i in range(1, len(have))) >= n
    
    def canPlaceFlowers3(self, flowerbed, n):
        slots = re.findall(r'0+', '0'+''.join(map(str, flowerbed))+'0')
        print(slots)
        sot = str('00')
        print(sum((len(sot)-1)/2))
        return sum((len(slot)-1)/2 for slot in slots) >= n
        

s = Solution()   
flowerbed = [0, 1, 0]
n = 1
print(s.canPlaceFlowers3(flowerbed, n))