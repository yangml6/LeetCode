class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        # n = len(nums)
        # return n * (n+1) / 2 - sum(nums)
        
        #用完整序列和，减去现有 nums 元素和，即为缺失的
        return sum(range(len(nums)+1)) - sum(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [0]
    print(s.missingNumber(nums))
