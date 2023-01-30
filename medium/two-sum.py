# Problem: https://leetcode.com/problems/two-sum/submissions/875835984/

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i 
