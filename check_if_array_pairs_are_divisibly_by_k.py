from collections import Counter
# @leet start
class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        """
        This question asks us whether or not we can divide the provided array
        into pairs where the sum of the numbers is divisible by k.

        To do this, we can calculate the modulo of each item and keep it in
        a counter. Then, note the following cases:
        1. If a modulo of 0 exists, it can only be paired by another 0.
        Imagine that the k is 5, and there are two items, 5 and 10. They both
        divide cleanly into k, so if paired together, they meet the condition.
        Thus, we must have an even number of items that have a remainder of 0.
        2. For any other case, we need to find its complement, where its mod is
        k - curr_mod.

        We apply this property for all the modulos and return if we made it through
        the entire hashmap properly.
        """
        if sum(arr) % k != 0:
            return False
        modulos = Counter([item % k for item in arr])

        if 0 in modulos:
            if modulos[0] % 2 != 0:
                return False
            del modulos[0]

        for key, count in modulos.items():
            complement = k - key
            if modulos[complement] != count:
                return False
        return True



# @leet end

def test():
	assert(2 + 2 == 4)
