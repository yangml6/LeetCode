class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class SolutionClassic:
    def reverseString(self, s):
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return "".join(r)

c1 = Solution()
c2 = SolutionClassic()
s = "hello"
out1 = c1.reverseString(s)
out2 = c2.reverseString(s)
print(out1, out2)
