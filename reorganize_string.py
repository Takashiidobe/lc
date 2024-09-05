from collections import Counter


# @leet start
class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        This question asks us to rearrange the characters of s so that no two
        adjacent characters are the same. The way we do this is putting the
        string into a counter, and making sure there's no majority element.
        In the case that there is a majority element, there's no way to rearrange
        the string such that no two adjacent characters are the same.

        In the other case, we can solve the problem. We just need to iterate
        through the string in most common order and then add to a string
        every two places, starting at 0, and looping back to 1. This makes
        it so no two adjacent characters will be the same.
        """
        c = Counter(s)
        n = len(s)
        most_common_count = c.most_common(1)[0][1]
        if n % 2 == 0 and most_common_count > n // 2:
            return ""
        if n % 2 == 1 and most_common_count > n // 2 + 1:
            return ""

        chars = [" "] * n

        i = 0

        for char, count in c.most_common():
            for _ in range(count):
                chars[i] = char
                if i + 2 < n:
                    i += 1
                else:
                    i = 1

        return "".join(chars)


# @leet end


def test():
    assert 2 + 2 == 4
