from functools import cache


# @leet start
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        This question gives us a decoding that isn't a prefix decoding, so
        sometimes the prefixes can overlap. Since we're encoding lowercase
        english letters, the message comes in 1-26, and since its a stream,
        we can decode each pair of letters more than one way if it falls in
        between 1 - 26.

        Also note that a leading '0' in a string is invalid, so if we chooose
        '11106' and pick '11', '1', '06', it is invalid. We would return 0
        in this case.

        So, for this question, we have a few conditions:
        1. If we've hit the end of the string, we return 1 for success.
        2. If our current character is a 0, return 0 for invalid decoding.

        Otherwise, we check the next two letters in the stream. If they decode
        to 1 - 26, we return the count of the decodings of if we took the next
        letter and the next two letters.

        Otherwise, we can just advance our pointer once.
        """

        @cache
        def dp(index, s):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index == len(s) - 1:
                return 1

            if int(s[index : index + 2]) <= 26:
                return dp(index + 1, s) + dp(index + 2, s)
            return dp(index + 1, s)

        return dp(0, s)


# @leet end


def test():
    assert 2 + 2 == 4
