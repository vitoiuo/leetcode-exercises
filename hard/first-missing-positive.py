def firstMissingPositive(nums):
    missing_int = set(range(1,len(nums)+1)) - set(nums)
    if bool(missing_int):
        return min(missing_int)
    return max(nums) + 1
