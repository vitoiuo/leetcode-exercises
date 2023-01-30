# Problem: https://leetcode.com/problems/first-missing-positive/submissions/877477815/
class Solution(object):
    def firstMissingPositive(self, nums):
        missing_int = set(range(1,len(nums)+1)) - set(nums)
        if missing_int:
            return min(missing_int)

        return max(nums) + 1
