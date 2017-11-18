class Solution(object):
#找最大差值
    #简单两层循环，time limit exceeded
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # lmax = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         sub = prices[j] - prices[i]
        #         lmax = max(lmax, sub)
            
        # return lmax

    def maxProfit2(self, prices):
        max_profit = 0
        min_price = prices[0]
        # min_price = float('inf')
        # print(min_price)

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit) 

        return max_profit

if __name__ =='__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    res = s.maxProfit2(prices)
    print(res) 
            
             



                
            
            