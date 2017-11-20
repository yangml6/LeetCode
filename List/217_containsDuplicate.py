class Solution(object):
    def containsDuplicate(self, nums):
        #判断是否有重复数字
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for index, num in enumerate(nums):
            dic[num] = index
        # print(len(dic), len(nums))
        if len(nums) == len(dic):
            return False
        else:
            return True

    def containsDuplicate2(self, nums):
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,3]
    print(s.containsDuplicate2(nums))
