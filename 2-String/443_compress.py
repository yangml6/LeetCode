class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read_index = 0
        write_index = 0
        l = len(chars)
        while(read_index < l):
            ch = chars[read_index]
            count = 0
            while(read_index < l and chars[read_index] == ch):
                read_index += 1
                count += 1
            chars[write_index] = ch
            write_index += 1
            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1
        return write_index
        
sol = Solution()
# s = ['a', 'a', 'a', 'b','b']
# s = ['a']
s = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ans = sol.compress(s)
print(ans)