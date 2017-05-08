#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation
#
# Medium (28.54%)
# Total Accepted:    107913
# Total Submissions: 377116
# Testcase Example:  '[1]'
#
# 
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <2:
            return
        j=len(nums)-2
        while j>=0 and nums[j]>=nums[j+1]:
            j = j-1

        if j<0:
            
            nums.sort()
            return
        i = j+1
        while i< len(nums) and nums[i] >nums[j]:
            i = i +1
        nums[j], nums[i-1] = nums[i-1] ,nums[j]
    
        nums[j+1:]=list(reversed(nums[j+1:]))
        return 
