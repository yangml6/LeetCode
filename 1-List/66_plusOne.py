#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:03:30 2017

@author: yml
"""
#用一个数组表示非负整数，+1，需要处理进位

class Solution(object):
#   def plusOne(self, digits):
#       digits = digits[::-1] 
#       print(digits)
#       
#       digits[0] += 1
#       
#       if len(digits) == 1:
#           if digits[0] >= 10:
#               digits[0] = 0
#               digits.append(1)
#           return digits[::-1]
#       
#       if digits[0] + 1 > 10:
#           digits[0] = 0
#           digits[1] += 1
#       for i in range(1, len(digits)-1):
#           if digits[i] >= 10:
#               digits[i] = 0
#               digits[i + 1] += 1
#       if digits[len(digits) - 1] >= 10:
#           digits[len(digits) - 1] = 0
#           digits.append(1)     
#           
#       return digits[::-1]
   
    def plusOne2(self, digits):
        #beats 3.54%
              
        plus1 = int(''.join(str(i) for i in digits)) + 1 # 1020 type:int
        
        seq = []
        
        for i in str(plus1):
            seq.append(int(i))
        return seq

#        return [int(t) for t in list(str(int(''.join([str(i) for i in digits])) + 1))]
 
    
#    def plusOne3(self, digits):
#        carry=1
#        for i in reversed(range(len(digits))):
#            #python3m没有xrange
#            digits[i]+=carry
#            carry=digits[i] / 10
#            digits[i] %= 10
#        if carry:
#            digits = [1] + digits
#        return digits

        
        
if __name__ == '__main__':
    digits = [1, 0, 1, 9]
    s = Solution()
    res = s.plusOne2(digits)
    print('*****Result:*****''\n',res)