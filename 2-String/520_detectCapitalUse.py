class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False

    def detectCapitalUse2(self, word):
        return word.isupper() or word.islower() or word.istitle()

    def detectCapitalUse3(self, word):
        return len(word)==1 or word[1:].islower() or word.isupper()

sol = Solution()
s = 'ABcabc'
ans = sol.detectCapitalUse(s)
print(ans)