class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int], not empty
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))


    def findDisappearedNumbers2(self, nums):
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]





if __name__ == '__main__':
    s = Solution()
    nums =[1,1]
    print(s.findDisappearedNumbers2(nums))