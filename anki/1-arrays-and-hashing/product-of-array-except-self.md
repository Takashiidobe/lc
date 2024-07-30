# 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

%

To solve this problem, we first create a prefix and suffix array, which
contain the prefix and suffix product of all items up to the current
number.

Finally, for each of the numbers, we multiply the previous prefix number
and the suffix index one after our current index. This returns us the
product of all the other numbers except our current number, and add that
to the array.

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] * num)

        suffix = [nums[-1]]
        for num in list(reversed(nums))[1:]:
            suffix.append(suffix[-1] * num)
        suffix.reverse()

        res = []
        for i, num in enumerate(nums):
            prefix_index = i - 1
            suffix_index = prefix_index + 2

            total = 1

            if 0 <= prefix_index < len(nums):
                total *= prefix[prefix_index]
            if 0 <= suffix_index < len(nums):
                total *= suffix[suffix_index]

            res.append(total)

        return res
```
