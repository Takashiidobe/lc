# @leet start
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """
        This question asks us to verify that the words provided are sorted according
        to an alien dictionary.
        We can do as the question asks, by sorting the words and making sure they
        align in $O(n log n)$ time.

        We can verify that words are properly sorted in $O(n)$ time, however.
        If we zip the words and make sure that both words are in the right order
        (l < r) for all words in the word list, the list is sorted.
        """

        dictionary = {c: i for i, c in enumerate(order)}

        # This is the $O(n log n) solution
        # return words == sorted(words, key=lambda word: [dictionary[c] for c in word])
        for l, r in zip(words, words[1:]):
            if [dictionary[c] for c in l] <= [dictionary[c] for c in r]:
                continue
            return False
        return True


# @leet end


def test():
    assert 2 + 2 == 4
