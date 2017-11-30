class Solution(object):
    def rotate(self, nums, k):
        #旋转,轮换
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

        # k = k % len(nums)
        # print(nums[-k:], nums[:-k])
        # nums[:] = nums[-k:] + nums[:-k]  

        #没有 return！要求修改 nums 本身，所以用nums[:],不能用 nums[]


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(s.rotate(nums, k))