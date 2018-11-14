#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:59:49 2017

@author: yml
"""
#删除 nums 中所有值为 val 的元素，不声明新数组

#O(n)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        newIndex = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newIndex] = nums[i]
                newIndex += 1
                
        return newIndex
    
#O(n2)

    def removeElement2(self, nums, val):
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 4, 4, 6]
    val = 4
    out = s.removeElement(nums, val)
    print(out)