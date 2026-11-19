class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        
        prefix = [1]
        for i in range(1, len(nums)):
            pref = nums[i - 1] * prefix[i - 1]
            prefix.append(pref)

        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result