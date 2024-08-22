from typing import Optional
from utils import ListNode


# @leet start
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list.
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


# @leet end


def test():
    assert 2 + 2 == 4
