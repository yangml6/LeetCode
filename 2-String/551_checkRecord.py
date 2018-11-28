class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = s.count('A') > 1
        late = 'LLL' in s
        if absent or late:
            return False
        else:
            return True
    def checkRecord2(self, s):
        return s.count('A') <= 1 and s.count('LLL') == 0