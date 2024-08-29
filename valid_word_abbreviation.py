# @leet start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        This question asks us to see if a pattern matches a word, where
        numbers inside the pattern means match any one character.

        So, we have to parse the abbreviation, without allowing leading zeroes,
        and if we see a character, we check if it matches and increment pointers
        if it does, otherwise, if its a number, parse the number and then skip
        the word pointer that many characters. If the characters doesn't match,
        return False, and at the end of the loop, if we haven't hit the end
        of both of the strings, return False.
        """
        i = j = 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n


# @leet end


def test():
    assert 2 + 2 == 4
