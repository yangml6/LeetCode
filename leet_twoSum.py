class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
#        for i in xrange(len(nums)):
#            for j in xrange(i,len(nums)):
#                if target - nums[i] == nums[j] and i != j:
#                    return [i,j]

        dict = {}

        for i,num in enumerate(nums):
            dict[num] = i

        for i,num in enumerate(nums):
            if target - num in dict and dict[target - num] != i:
                return [i,dict[target - num]]

