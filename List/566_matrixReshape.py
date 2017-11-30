class Solution(object):
    #二维数组
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums_ = []
        r_ = len(nums)
        c_ = len(nums[0])
        if r_*c_ < r*c :
            return nums
        for i in range(c_):
            for j in range(r_):
                nums_.append(nums[i][j])
        for i in range(r):
            nums[i] = nums_[i*c : (i+1)*c]
        return num[:r]

if __name__ == '__main__':
    s = Solution()
    # nums =[1,1,0,1,1,1]
    nums = [[1,2],
            [3,4]]
    r = 4
    c = 1
    print(s.matrixReshape(nums, r, c))