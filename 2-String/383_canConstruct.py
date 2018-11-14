import collections
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = collections.Counter(ransomNote)
        magazine = collections.Counter(magazine)
        return ransomNote - magazine 
       
sol = Solution()
ransomNote = "fffbfg"
# ransomNote = 'a'
magazine = "effjfggbffjdgbjjhhdegh"
# magazine = 'b'
ans = sol.canConstruct(ransomNote, magazine)
print(ans)