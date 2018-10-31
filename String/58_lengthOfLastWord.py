class Solution:
    def lengthOfLastWord1(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ').split(' ')
        print(s)
        return len(s[-1])

    def lengthOfLastWord2(self, s):
        start, res = 0, 0
        calc = True
        s += " "
        for i in range(len(s)):
            cur = s[i]
            if cur == ' ' and calc: 
                res = i-start
                calc = False
            elif cur != ' ' and not calc:
                start = i
                calc = True
        return res        

sol = Solution()
s = ' '
ans = sol.lengthOfLastWord1(s)
print(ans)