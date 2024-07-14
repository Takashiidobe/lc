from collections import Counter


# @leet start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        To find the top k most frequent elements, one way is to sort the elements
        in $O(n{}log{}n)$ time to have all the items next to each other.
        Then, we would do a groupby, so we could have a key -> value pair of
        item to frequency. Finally, we could sort that groupby again in descending
        order and then return that.

        However, there's a faster way using a heap. We can find the frequency of
        each item by using a hashmap in $O(n)$ time, and then popping off the most
        common ones in $O(log{}n)$ time, and doing that $k$ times for a complexity
        of $O(n{}log{}k)$ time.

        There is a better way that involves grouping using a hashmap and then quickselecting
        in $O(n)$ time but I didn't do that for this question.
        """
        c = Counter(nums)

        return [x[0] for x in c.most_common(k)]


# @leet end
sol = Solution()


def test():
    assert sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert sol.topKFrequent([1], 1) == [1]
