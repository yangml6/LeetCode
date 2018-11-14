import collections
class Solution(object):
    
    def findPairs(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res   





if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]
    k = 0
    print(s.findPairs(nums, k))