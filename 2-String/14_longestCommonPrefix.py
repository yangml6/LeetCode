class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        def samePre(self, str_, same_pre):
            length = min(len(str_), len(same_pre))
            same_pre = same_pre[:length]
            if length == 0:
                return ''
            for i in range(length):
                if same_pre[i] == str_[i]:
                    pass
                else:
                    same_pre = same_pre[:i]
                    break
            return same_pre
        
        same_pre = strs[0]                   
                
        for i in range(len(strs)):
            same_pre = samePre(self, strs[i], same_pre)

        return same_pre

            
        # if not strs: return ''
		# 		#since list of string will be sorted and retrieved min max by alphebetic order
        # s1 = min(strs)
        # s2 = max(strs)
        # print(s1, s2)

        # for i, c in enumerate(s1):
        #     if c != s2[i]:
        #         return s1[:i] #stop until hit the split index
        # return s1




        
sol = Solution()
strs = ["flower","flow","flight","aa"]
# strs = ['aa', 'a']
ans = sol.longestCommonPrefix(strs)
print(ans)