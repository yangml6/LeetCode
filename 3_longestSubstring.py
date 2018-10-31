class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}

        # for i in range(len(s)):
        #     if s[i] in usedChar and start <= usedChar[s[i]]:
        #         start = usedChar[s[i]] + 1
        #     else:
        #         maxLength = max(maxLength, i - start + 1)
        # usedChar[s[i]] = i
        # return maxLength

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

        






        

so = Solution()    
s = 'abcabcbb'
res = so.lengthOfLongestSubstring(s)
print(s)