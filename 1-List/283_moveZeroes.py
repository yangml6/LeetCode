class Solution(object):
    def moveZeroes(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0：
                #遇见0记录下位置,遇到不为0交换，遇见0之前等于自身交换
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        return nums
    

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    # nums = [2,1]
    s = Solution()
    print(s.moveZeroes(nums))