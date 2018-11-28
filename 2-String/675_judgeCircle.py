import collections
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr = moves.count('L') == moves.count('R')
        ud = moves.count('U') == moves.count('D')
        if lr and ud:
            return True
        else:
            return False
    
    def judgeCircle2(self, moves):
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']