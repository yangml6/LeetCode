class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        mapping = {")":"(", "]":"[", "}":"{"}
        # mapping = {"(":")", "[":"]", "{":"}"} # 错
        
        for char in s:

            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'
                # The mapping for the opening bracker in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracker, simply push it onto the stack
                stack.append(char)
            
            # In the end, if the stack is empty, then we have a valid expression
        return not stack

sol = Solution()
s = "(()){}[]"
ans = sol.isValid(s)
print(ans)