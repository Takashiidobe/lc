# @leet start
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        The solution that meets this problem is floyd's tortoise and hare
        algorithm.
        We first start out by finding the cycle in nums by having a slow and fast
        pointer, and breaking out when they intersect.

        Next, we make both the tortoise and the hare travel at the same speed,
        starting the tortoise from the start and the hare at the intersection.
        Next, have both of them set to the value of their index, and return
        either the tortoise or the hare when they're equal.
        """
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

    def cyclic_sort(self, nums: list[int]) -> int:
        """
        This solution involves cyclically sorting the array.
        At every iteration of the loop, we pick the first item of the array,
        nums[0] and compare it to what is in its index, i.e. nums[nums[0]].

        We then swap these as long as they aren't the same, and continue.

        This works, becuase we know that 0 isn't in the array. We also know
        that only items with a duplicate will match the condition of
        nums[0] == nums[nums[0]] because there needs to be at least two
        of the same item in the array for this to be the case.

        For an example, say [1, 2, 3, 3].
        We take 1, and check what's in its index, 2.
        We see they are different, so we swap them:
        [2, 1, 3, 3]
        Next, we look at the index of 2, which is not 2, so we swap.
        [3, 1, 2, 3]
        Now, we check the 3rd index and find that it matches 3.
        Thus, we've found the duplicate, and can return either
        nums or nums[nums[0]].
        """
        while nums[0] != nums[nums[0]]:
            nums[0], nums[nums[0]] = nums[nums[0]], nums[0]

        return nums[0]


# @leet end


def test():
    assert 2 + 2 == 4
