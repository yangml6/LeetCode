class Solution(object):
    # def __init__(self,nums):
    #     #self.nums = nums
        

    def majorityElement(self, nums):

        #找众数，假设众数一定存在
        """
        :type nums : list[int]
        :rtype: int
        """
        length = len(nums)
        dic = {}
        dic2 = {}

        for index,num in enumerate(nums):
            if num not in dic:
                dic2[num] = 0
                #print(dic2[num])
            dic[num] = index 
        
        for index,num in enumerate(nums):
            if num in dic:
                dic2[num] += 1
                #print(dic2[num])
            dic[num] = index 

        for key, value in dic2.items():
            if dic2[key] >= length/2:
                return key
    
    def majorityElement2(self, nums):
        #因为假设众数存在，排序后中间位置一定是
        l = len(nums)//2#两个
        return sorted(nums)[l]

    




if __name__ == '__main__':
    s = Solution()
    nums = [1,2,2,3]
    print(s.majorityElement2(nums))
