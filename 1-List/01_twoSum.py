class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
#solution1         
#        for i in xrange(len(nums)):
#            for j in xrange(i,len(nums)):
#                if target - nums[i] == nums[j] and i != j:
#                    return [i,j]

#solution2
        dict = {}

        for i,num in enumerate(nums):
            dict[num] = i

        for i,num in enumerate(nums):
            if target - num in dict and dict[target - num] != i:
                return [i,dict[target - num]]


#solution3
        dict = {}
        for i,num in enumerate(nums):
            if target - num in dict:
                return [i,dict[target-num]]
            else:
                dict[num] = i
