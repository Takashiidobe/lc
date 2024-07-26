from typing import Optional
from utils import ListNode
# @leet start


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        To reverse a linked list, we want to keep two pointers, `prev` and `curr`
        where `prev` refers to the previous pointer (or None) and `curr` refers to
        the head of the linked list.
        We then advance the linked list by taking the next and storing it in a temporary
        variable, and then setting prev to curr and curr.next to prev (to reverse the list)
        next, we set curr to the temporary variable and do that for every variable,
        and at the end we return the prev pointer, which now holds the reversed list.
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            prev = curr
            curr.next = prev
            curr = next_temp
        return prev


# @leet end


def test():
    assert 2 + 2 == 4
