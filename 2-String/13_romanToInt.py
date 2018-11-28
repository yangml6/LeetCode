class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        s = s[::-1]
        allSum = dic[s[0]] 
        for i in range(1, len(s)):
            if dic[s[i-1]] <= dic[s[i]]:
                allSum += dic[s[i]]
            else:
                allSum -= dic[s[i]]
        return allSum

sol = Solution()
s = 'IVV'
ans = sol.romanToInt(s)
print(ans)


