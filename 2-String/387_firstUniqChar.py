import string
class Solution:
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

    def firstUniqChar2(self, s):
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
    
sol = Solution()
s = 'leetcodel'
print(s.rpartition('t'))
ans = sol.firstUniqChar2(s)
print(ans)
