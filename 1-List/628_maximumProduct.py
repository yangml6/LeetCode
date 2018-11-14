class Solution:
    def maximumProduct(self, nums):
    #找到乘积最大的三个数，问题点在于有负数情况
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(nums)
        n = sorted(nums)
        maximum =max( n[-1] * n[-2] * n[-3],
                    n[-1] * n[0] * n[1])
        return maximum

s = Solution()
nums = [-4,-3,-2,-1,60]
maximum = s.maximumProduct(nums)
print(maximum)