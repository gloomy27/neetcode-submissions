class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        result = []

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in hashmap:
            buckets[hashmap[num]].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

    
        return result [:k]