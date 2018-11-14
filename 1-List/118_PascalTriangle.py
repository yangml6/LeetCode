class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # resList = [[1]]

        # # resList[0] = [1]
        # i = 1
        # j = 0

        # while i < numRows:
        #     while j < i:
        #         if j == 0 or j == i:
        #             resList[i]+= 1
        #         else:
        #             resList[i]+=9
        #         j += 1
        #     i += 1
        
        # return resList



        if not numRows: 
            return []
        ret = [[1]]
        numRows -= 1
        while numRows:
            ret.append([1] + [a+b for a,b in zip(ret[-1][:-1], ret[-1][1:])] +[1])
            numRows-=1
        return ret

    def generate2(self, numRows):
        if numRows <= 0:
            return []
        triangle = [[1]]
        
        for i in range(1, numRows):
            row = [0] + triangle[-1] + [0]
            print(triangle[-1])
            triangle.append([row[j] + row[j+1] for j in range(i+1)])
             
        return triangle

if __name__ == '__main__':
    s = Solution()
    numRows = 5
    res = s.generate2(numRows)
    print(res)
            