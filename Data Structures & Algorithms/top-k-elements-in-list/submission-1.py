class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        return sorted(hashmap, key=lambda num: hashmap[num], reverse=True)[:k]