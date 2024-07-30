# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

%

To group anagrams together, we can use a Counter and a hashmap (in this
case, a defaultdict to shorten up the code).

For each word in strs, we add it to the hashmap, but making sure to add
its counter form to the dict as a key, and itself as the value.

At the end, we just have to return the values grouped, so a list of the
defaultdict's values will suffice.

```python
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = frozenset(Counter(s).items())
            anagrams[key].append(s)

        return list(anagrams.values())
```
