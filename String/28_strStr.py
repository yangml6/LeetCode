class Solution:
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(needle)
        b = len(haystack)
        i = 0
        while a <= b:
            if needle == haystack[i:i+a]:
                return i
            i += 1
            b -= 1
            
        else:
            return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1