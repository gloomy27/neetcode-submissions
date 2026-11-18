class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hashmap = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord not in hashmap:
                hashmap[sortedWord] = []

            hashmap[sortedWord].append(word)

        return list(hashmap.values())