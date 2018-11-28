class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        n = []
        for word in s:
            n.append(word[::-1])
        return ' '.join(n)
    def reverseWords2(self, s):
        return ' '.join(s.split()[::-1])[::-1]
    def reverseWords3(self, s):
        return ' '.join(x[::-1] for x in s.split())