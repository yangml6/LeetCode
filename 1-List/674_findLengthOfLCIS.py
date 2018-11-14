class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_max = final_max = 1
        length = len(nums)
        if length == 0:
            return 0
        for i in range(length-1):
            if nums[i] < nums[i+1]:
                temp_max += 1
                final_max = max(temp_max, final_max)
            else:
                temp_max = 1
        return final_max
    
s = Solution()
# nums = [1, 3, 5, 4, 7]
nums = [2, 2, 2, 2]
ans = s.findLengthOfLCIS(nums)
print(ans)