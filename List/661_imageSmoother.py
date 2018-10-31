import math
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # R, C = len(M), len(M[0])
        # print(R,C)
        
        # ans = [[0]*C for _ in M] # python 允许 _ 作为一个变量，和 x、i 一样
        # for r in range(R):
        #     for c in range(C):
        #         count = 0
        #         for nr in (r-1, r, r+1):
        #             for nc in (c-1, c, c+1):
        #                 if 0 <= nr < R and 0 <= nc < C:
        #                     ans[r][c] += M[nr][nc]  # 格内数字
        #                     count += 1            # 有几个格
        #         ans[r][c] /= count   # 取整
        # return ans
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] = math.floor(ans[r][c]/count)

        return ans

s = Solution()        
M = [[1,1,1],
     [1,0,1],
     [1,1,1]]
ans = s.imageSmoother(M)
print(ans)