#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle/description/
#
# algorithms
# Easy (68.43%)
# Total Accepted:    80.8K
# Total Submissions: 118.1K
# Testcase Example:  '"UD"'
#
#
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place.
#
#
#
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
#
#
# Example 1:
#
# Input: "UD"
# Output: true
#
#
#
# Example 2:
#
# Input: "LL"
# Output: false
#
#
#


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vert = 0
        hor = 0
        for m in moves:
            if m == "R":
                vert += 1
            elif m == "L":
                vert -= 1
            elif m == "D":
                hor += 1
            else:
                hor -= 1
        return hor == 0 and vert == 0