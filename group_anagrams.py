from collections import defaultdict, Counter


# @leet start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = frozenset(Counter(s).items())
            anagrams[key].append(s)

        return list(anagrams.values())


# @leet end

