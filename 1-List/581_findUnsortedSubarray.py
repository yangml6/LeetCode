class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minus = 0
        s_nums = sorted(nums)
        l = len(nums)
        for i in range(l):
            if s_nums[i] == nums[i]:
                minus += 1
            else:
                break
        for i in range(l):
            if s_nums[l-i-1] == nums[l-i-1]:
                minus += 1
            else:
                break
        if l>minus: #防止计算了两次
            return l-minus
        else:
            return 0




s = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [5,4, 3, 2, 1]
print(s.findUnsortedSubarray(nums))