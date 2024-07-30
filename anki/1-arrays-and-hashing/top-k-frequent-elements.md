# 347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]


%

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

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        """
        c = Counter(nums)

        return [x[0] for x in c.most_common(k)]
```
