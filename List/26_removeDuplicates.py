#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:14:29 2017

@author: yml
"""
#题目要求使用连续空间，不允许声明新数组,返回长度
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums :
            return 0
        
        newTail = 0;
        
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1





#若声明一个新的数组 pure
#def removeDuplicates2(nums):
#    """
#    :type nums: List[int]
#    :rtype: int
#    """
#    pure = []
#    count = 0
#    
#    for index,num in enumerate(nums):
#        if num in pure:
#            pass
#        else:
#            pure.append(num)
#            count += 1
#        
#    return pure
#
if __name__ =='__main__':
   nums = [1,1,2,3,5,6]
   s = Solution()
   nu = s.removeDuplicates(nums)
   print(nu)