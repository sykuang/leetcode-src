#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number
#
# Easy (38.87%)
# Total Accepted:    98748
# Total Submissions: 253529
# Testcase Example:  '-2147483648'
#
# 
# Write a program to check whether a given number is an ugly number.
# 
# 
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another
# prime factor 7.
# 
# 
# 
# Note that 1 is typically treated as an ugly number.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        elif num < 7:
            return True
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        if num != 1:
            return False
        else:
            return True

