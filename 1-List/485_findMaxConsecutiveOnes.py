class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int], a binary array
        :rtype: int
        """
        count = max_ = 0
        for i in nums:
            if i == 1:
                count += 1
                max_ = max(max_, count)
            else:
                count = 0
        return max_



if __name__ == '__main__':
    s = Solution()
    nums =[1,1,0,1,1,1]
    print(s.findMaxConsecutiveOnes(nums))