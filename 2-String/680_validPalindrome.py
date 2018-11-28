import collections
class Solution:
    def validPalindrome3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))
        
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True

    def validPalindrome2(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left+1:right+1]
                return one == one[::-1] or two[::-1]
            left, right = left+1, right-1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time limited exceeded
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            snew = s[0:i] + s[i+1:]
            print(snew)
            if snew == snew[::-1]:
                return True
        return False 
    

sol = Solution()
s = 'abca'

ans = sol.validPalindrome2(s)
print(ans)
