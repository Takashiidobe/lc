from itertools import chain


# @leet start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Given a string of digits, this question asks us to return the letter
        combinations it can create.

        To do this, we first create a mapping of digit -> possible letters.

        Then, for the starting digit, we flatten the list of possible letters
        and use that as our starting list.

        For every subsequent digit, we iterate through the current combinations
        and extend the current set by appending each of the letters to all of the
        current items in our set.
        """
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        for k, v in mapping.items():
            mapping[k] = list(v)

        res = chain(mapping[digits[0]])

        for c in digits[1:]:
            new_res = []
            for combination in res:
                new_res.extend([combination + letter for letter in mapping[c]])
            res = new_res

        return res


# @leet end


def test():
    assert 2 + 2 == 4
