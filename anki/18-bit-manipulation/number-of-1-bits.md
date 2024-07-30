# 191. Number of 1 Bits

Write a function that takes the binary representation of a positive integer and returns the number of
set bits
it has (also known as the Hamming weight).

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.



Constraints:

    1 <= n <= 231 - 1


Follow up: If this function is called many times, how would you optimize it?

%

The count of one bits in a number can be done by bitwise ANDing the
number `n` with itself minus 1 `n - 1`.
The reason why this works is that if a bit is set in `n`, in `n - 1`,
its least significant bit will become 0.
Thus, if we AND the numbers together, the least significant bit is removed.
We count how many times we do this until the number hits 0 to remove
all of the one bits.

To optimize this function, we can use lookup tables.

Depending on how much memory we have, we can use more or less memory.

Say we want to see how many bits are set in an 8-bit number, we can
generate a lookup table that costs 256 bytes and index into it to see how
many 1 bits there are.

For a 64-bit number, however, this would cost 2^64 bytes, or 4GB.
For even bigger numbers, this would be excessive. To tune that, we could
chop the larger word into 8-bit chunks (so 8 chunks for a 64-bit
number), find out the number of 0s for each section, and then add them
up to find the final answer.

This also is easily to parallelize, and costs only 256 bytes for the
lookup table, so it retains good speed and memory usage.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count
```
