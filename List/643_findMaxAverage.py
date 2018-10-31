class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # #  Time Limit Exceeded
        # max = -50000
        # length = len(nums)
        # if length > k:
        #     for i in range(0,len(nums)-k+1):
        #         s = sum(nums[i:i+k])
        #         if s > max:
        #             max = s
        #     res = max/k
        #     print(res,'res')
        # else:
        #     res = sum(nums)/length
        # return res

        # # sliding window
        summ = sum(nums[:k])
        maximum = summ
        for i in range(1, len(nums)-k+1):
            summ -= nums[i-1]
            summ += nums[i+k-1]
            maximum = max(maximum, summ)
        return maximum/k

s = Solution()
nums = [0,1]
k = 4
r = s.findMaxAverage(nums, k)
print(r)
