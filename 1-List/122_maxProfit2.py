class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_ = 0
        #[6, 2, 4, 5, 3, 7, 9]
        price = []
        for i in range(1, len(prices)):
            sub = prices[i] - prices[i - 1]
            if sub > 0:
                max_ = max_ + sub
                i += 1
            else:
                pass
            
        return max_
                




if __name__ =='__main__':
    s = Solution()
    prices = [7, 3, 5, 3, 6, 4]
    #excepted 5
    res = s.maxProfit(prices)
    print(res) 