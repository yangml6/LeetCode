class Solution(object):

#两个sorted 整型List A、B，长度分别为 m、n,假设 A 有足够空间容纳 A + B, m之外的空间初始化为0

    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """
    #     while n > 0:
    #         if m <= 0 or nums2[n-1] >= nums1[m-1]:  
    #             nums1[m+n-1] = nums2[n-1]
    #             n -= 1
    #         else:
    #             nums1[m+n-1] = nums1[m-1]
    #             m -= 1

    def merge2(self, nums1, m, nums2, n):
        x = nums1[0 : m]
        y = nums2[0 : n]
        x.extend(y)
        x.sort()
        nums1[0 : m + n] = x
    
    def merge3(self, nums1, m, nums2, n):
        #amazing!
        nums1[m:] = nums2[:n]
        nums1.sort()

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    #expected:[1, 2, 2, 3, 5, 6]
    s.merge3(nums1, m, nums2, n)
    print(nums1)
