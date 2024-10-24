from functools import cache
# @leet start
class Solution:
	def minExtraChar(self, s: str, dictionary: list[str]) -> int:
		"""
		This question asks us to figure out how to create the minimum string given
		a dictionary where you can remove a substring if it exists in the dictionary.
		We can use every word in the dictionary as many times as we want to.

		We can look at this as an edit distance-esque question:
		1. Given an empty string, we return 0, since there are 0 extra characters.
		2. If the string is not empty, we try to match any of the words in the dictionary,
		starting at the beginning of the string. If we find a match, we recurse with that
		substring, trying to find the smallest resulting string.
		3. We also check what happens if we skip the current string, so we increment
		our pointer into the string by one and return the dfs of its result + 1.

		At the end, the minimum dfs length is the one we want to keep.
		"""
		@cache
		def dfs(s):
			if not s:
				return 0
			dfses = []
			skip = dfs(s[1:]) + 1
			for word in dictionary:
				if s.startswith(word):
					dfses.append(dfs(s[len(word):]))
			dfses.append(len(s))
			dfses.append(skip)
			return min(dfses)
		return dfs(s)


# @leet end

def test():
	assert(2 + 2 == 4)
