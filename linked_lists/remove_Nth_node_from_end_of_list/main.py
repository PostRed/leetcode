# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        data = []
        cur = head
        while cur:
            data.append(cur)
            cur = cur.next
        if len(data) == 1:
            return None
        if len(data) == n:
            return data[1]
        if n > 1:
            data[len(data) - n - 1].next = data[len(data) - n + 1]
        else:
            data[len(data) - n - 1].next = None
        return data[0]
