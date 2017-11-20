class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        #两个元素相同，且下标差值小于 k
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        #默认 return False
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [1,0,1,1]
    k = 1
    print(s.containsNearbyDuplicate(nums, k))
