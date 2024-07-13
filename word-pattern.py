# @leet start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        This problems involves defining a bijection (1:1) mapping between the words in `s` and the pattern.
        To do this, we split up the `s` into words, and then start iterating through both of them.
        If they both always equal each other, then we return true, otherwise, return false.
        """
        pattern_to_word = {}
        word_to_pattern = {}
        words = s.split(' ')
        # bail early
        if len(pattern) != len(words):
            return False

        for i, word in enumerate(words):
            curr_pattern = pattern[i]
            if curr_pattern not in pattern_to_word and word not in word_to_pattern:
                pattern_to_word[curr_pattern] = word
                word_to_pattern[word] = curr_pattern
                continue
            if curr_pattern not in pattern_to_word or word not in word_to_pattern:
                return False
            if pattern_to_word[curr_pattern] != word or word_to_pattern[word] != curr_pattern:
                return False

        return True
# @leet end
sol = Solution()

def test():
	assert(sol.wordPattern("abba", "dog cat cat dog") == True)
	assert(sol.wordPattern("abba", "dog cat cat fish") == False)
	assert(sol.wordPattern("aaaa", "dog cat cat dog") == False)
	assert(sol.wordPattern("abba", "dog dog dog dog") == False)
