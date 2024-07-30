# 136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.


%

In an array where each number is present twice except for one number,
this function finds that number.
The way it does this is by using xor.
If you xor a number by itself, you get 0.
So all of the numbers that show up twice reduce to 0, and the only number
that shows up once remains.

```python
from functools import reduce

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
```
