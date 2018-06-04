#
# [818] Similar RGB Color
#
# https://leetcode.com/problems/similar-rgb-color/description/
#
# algorithms
# Easy (53.23%)
# Total Accepted:    3.6K
# Total Submissions: 6.7K
# Testcase Example:  '"#09f166"'
#
# In the following, every capital letter represents some hexadecimal digit from
# 0 to f.
#
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
# For example, "#15c" is shorthand for the color "#1155cc".
#
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB -
# UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
#
# Given the color "#ABCDEF", return a 7 character color that is most similar to
# #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"
#
#
# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64
# -9 -0 = -73.
# This is the highest among any shorthand color.
#
#
# Note:
#
#
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0
# to f
# Any answer which has the same (highest) similarity as the best answer will be
# accepted.
# All inputs and outputs should use lowercase letters, and the output is 7
# characters.
#
#
#


class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        res = "#"
        for i in xrange(1, 6, 2):
            div, mod = divmod(int((color[i:i+2]),16), 17)
            if mod > 8:
                div += 1
            res += "%x%x" %(div,div)
        return res