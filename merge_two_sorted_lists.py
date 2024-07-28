from utils import ListNode
from typing import Optional


# @leet start
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        To merge two sorted lists, we first create a dummy node, and then refer
        to it to iterate through the list.
        and then, while both lists are non-null, we choose the lower value and
        add it to the list.
        Otherwise, one of the lists is non-empty, and if that's the case, we
        append that to the end of our current list.
        At the end, we return the next node of the list.
        """
        head = ListNode()
        curr = head

        # then for each item in
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head.next


# @leet end


def test():
    assert 2 + 2 == 4
