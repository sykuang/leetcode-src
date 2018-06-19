#
# [835] Linked List Components
#
# https://leetcode.com/problems/linked-list-components/description/
#
# algorithms
# Medium (50.26%)
# Total Accepted:    4.4K
# Total Submissions: 8.7K
# Testcase Example:  '[0,1,2,3]\n[0,1,3]'
#
# We are given head, the head node of a linked list containing unique integer
# values.
#
# We are also given the list G, a subset of the values in the linked list.
#
# Return the number of connected components in G, where two values are
# connected if they appear consecutively in the linked list.
#
# Example 1:
#
#
# Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
#
#
# Example 2:
#
#
# Input:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation:
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the
# two connected components.
#
#
# Note:
#
#
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N -
# 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        res = len(G)
        arr = []
        setG = set(G)
        pre = None
        while head:
            if pre is not None and pre in setG and head.val in setG:
                res -= 1
            pre = head.val
            head = head.next
        return res
