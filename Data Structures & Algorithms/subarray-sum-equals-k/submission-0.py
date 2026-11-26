class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        hashmap = {0: 1}

        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            result += hashmap.get(current_sum -k, 0)
            hashmap[current_sum] = 1 + hashmap.get(current_sum, 0)

        return result