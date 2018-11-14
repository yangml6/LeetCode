class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i%2 == 0:
                res += nums[i]
            else:
                pass
        return res

    def arrayPairSum2(self, nums):
        return sum(sorted(nums)[::2])

if __name__ == '__main__':
    s = Solution()
    # nums =[1,1,0,1,1,1]
    nums = [1,4,3,2]
    print(s.arrayPairSum(nums))