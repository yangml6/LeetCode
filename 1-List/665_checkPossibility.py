class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        count = 0
        max_h = max_t = 0
        if length == 1:
            return False
        for i in range(length-1):
            if nums[i] < nums[i+1]:
                max_h = nums[i]                                              
                max_t = nums[i+1]
                if 
            else:
                count += 1
        if count>1:
            return False
        else:
            return True

s = Solution()        
M = [3,4,2,3]
ans = s.checkPossibility(M)
print(ans)




