import re
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # way 1
        return sum(s[i] != ' ' and (i == 0 or s[i-1] == ' ') for i in range(len(s)))
        # way 2
        # return len(s.split(' '))
    

sol = Solution()
s = "h h "
ans = sol.countSegments(s)
print(ans)