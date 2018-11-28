class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= 2*k:
            return s[k-1::-1] + s[k:]
        for i in range(len(s)):
            if(i%(2*k) == 0):
                s = s[0:i] + s[i:i+k][::-1] + s[i+k:]
                # print(s[0:i] , s[i:i+k][::-1] , s[i+k:])
        return s
    def reverseStr2(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
    def reverseStr3(self, s, k):
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""


sol = Solution()
s = "abcdefg"
k = 2
ans = sol.reverseStr3(s, k)
print(ans)