#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:13:44 2017

@author: yml
"""
#将 target 插入 nums 中，找到已存在或需要插入的位置
class Solution(object):
    def searchInsert(self, nums, target):
        #beats 84%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        if target in nums: 
            index = nums.index(target)
        elif target > nums[len(nums) - 1]:
            index = len(nums)
        elif target < nums[0]:
            index = 0
            
        else:
            for i in range(len(nums)):
                if target < nums[i] and target > nums[i-1]:
                    index = i
                    
        return index
    
    
    def searchInsert2(self, nums, target):
        return len([x for x in nums if x<target])

    

if __name__ == '__main__':
    nums = [1,3]
    target = 2
    
    index = Solution()#创建类实例
    
    res = index.searchInsert(nums, target)
    res2 = index.searchInsert2(nums, target)
    
    print(res, res2)
    
    