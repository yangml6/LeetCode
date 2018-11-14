import re
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        snew = s.strip(' ')
        sne = re.split(r" +", snew).remove('')
        print(sne)
        count = len(sne)
        return count 
    

sol = Solution()
s = "    "
ans = sol.countSegments(s)
print(ans)