class Solution:
    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s*2)[1:-1]
        return s in ss 
    def repeatedSubstringPattern2(self, s):
        length = len(s)
        if length <= 1:
            return False
        for i in range(1, length//2+1):
            if length %i == 0:
                str = s[i:] + s[0:i]
                if str == s:
                    return True
        return False




sol = Solution()
s = 'abcabc'
ans = sol.repeatedSubstringPattern1(s)
print(ans)