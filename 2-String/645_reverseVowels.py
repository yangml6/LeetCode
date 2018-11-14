import re
class Solution:
#     def reverseVowels1(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         temp = 'aeiouAEIOU'
#         l, r = 0, len(s) - 1
#         while l < r :
#             while l<r and s[l] not in temp:
#                 l += 1
#             while l<r and s[r] not in temp:
#                 r -= 1
#             if l < r:
#                 s = s[0:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
#             l += 1; r -= 1
#         return s
# #'str' object doesn't support item assignment  
    
    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

sol = Solution()
s = 'aA'
ans = sol.reverseVowels(s)
print(ans)
#print : holle