from utils import ListNode
from typing import Optional


# @leet start
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        To remove the nth node from the end, create a dummy pointer, and then
        iterate the fast pointer n + 1 times to make it n + 1 positions faster
        than the slow pointer. Finally, advance the slow and fast pointer in tandem,
        and then when the fast pointer is None, we skip slow.next's pointer and
        set it to slow.next.next.

        Finally, we return the dummy pointer's next (the old head) to complete
        the removal.
        """
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


# @leet end


def test():
    assert 2 + 2 == 4
