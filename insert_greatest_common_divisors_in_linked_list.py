from utils import ListNode
from typing import Optional

# @leet start
from math import gcd


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        This question asks us to insert the gcd of pairs of items in between nodes
        We can do this by having a slow pointer and fast pointer that are
        next to each other. We then take both their values, calculate their gcd,
        and insert a new node in between them.
        So, imagine this list:

        18 -> 6 -> 3
        We would want to insert 6 and 3 in between:
        18 -> 6 -> 6 -> 3 -> 3
        So we set up a fast and slow pointer:
        18 -> 6
        ^     ^
        And then we take both their values, calculate their gcd and create a new node.
        We then set slow.next to the new node, and then connect the new node
        to the fast node. Finally, we set slow equal to fast (to jump over the
        new node) and increment the fast pointer.

        At the end we return our copy of the head node.
        """
        if not head:
            return None
        dummy = slow = fast = head
        fast = fast.next

        while slow and fast:
            gcd_node = ListNode(gcd(fast.val, slow.val))
            slow.next = gcd_node
            gcd_node.next = fast
            slow = fast
            fast = fast.next
        return dummy


# @leet end


def test():
    assert 2 + 2 == 4
