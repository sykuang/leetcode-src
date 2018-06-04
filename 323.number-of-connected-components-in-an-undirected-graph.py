#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (49.12%)
# Total Accepted:    38.2K
# Total Submissions: 77.8K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
#
# Example 1:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4
#
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
#
# Output:  1
#
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#
#


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = range(n)

        def find(a):
            root = a
            while root != parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 != p2:
                parent[p1] = p2
        for a, b in edges:
            union(a, b)
        components = set()
        for i in xrange(n):
            components.add(find(i))
        return len(components)
