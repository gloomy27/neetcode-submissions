class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        count = 0
        maxCount = count

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                while num + count in nums_set:
                    count += 1
            maxCount = max(count, maxCount)

        return maxCount