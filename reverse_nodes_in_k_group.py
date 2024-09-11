from typing import Optional
from utils import ListNode


# @leet start
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reversed_head = self.reverse_linked_list(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversed_head
        return head

    def reverse_linked_list(self, head, k):
        new_head, ptr = None, head

        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head


# @leet end


def test():
    assert 2 + 2 == 4
