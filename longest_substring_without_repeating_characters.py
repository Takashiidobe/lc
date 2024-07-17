from collections import Counter


# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        To calculate the length of the longest substring, we want to
        create a sliding window, where the current window does not have
        any repeating characters.

        To handle this, we have 3 variables, a left and right pointer,
        and a Counter, which counts the chars that are included.

        If two of the same char are encountered, then we keep advancing the left
        pointer until we either reach the right pointer or we've removed
        the second time the char was included.

        For each iteration, we check to see if it's the max length we've seen so far
        and continue on.

        """
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


# @leet end


def test():
    assert 2 + 2 == 4
