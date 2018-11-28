class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == '' or b == '':
            return ''
        if len(a) <= len(b):
            s1, s2 = a, b
        else:
            s1, s2 = b, a
        lus = 0
        for i in range(len(s1)):
            for j in range(len(s1[i:])+1):
                if s1[i:i+j] not in s2:
                    print(i, j, s1[i:i+j])
                    temp = len(s1[i:i+j])
                    lus = max(temp, lus)
        if lus > 0:
            return lus
        else:
            return -1

sol = Solution()
a = "aefawfawfawfaw"
b = "aefawfeawfwafwaef"
ans = sol.findLUSlength(a, b)
print(ans)
    