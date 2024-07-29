from utils import ListNode
from typing import Optional


# @leet start
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        To figure out if a linked list has a cycle, we can do the following:
        We first know that linked lists that dont have a head and a pointer cannot
        have cycles (since they have 0 or 1 elements), and cannot create a self-cycle.

        We iterate the slow pointer by one and the fast pointer by two, and then
        check if they intersect. If they don't intersect, there's no cycle.

        If they do intersect, there is a cycle.
        """
        # A linked list without a next pointer can't have cycles
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        # this is unreachable
        return False


# @leet end
def test():
    assert 2 + 2 == 4
