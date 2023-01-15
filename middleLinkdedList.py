class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = result = head
        while start and start.next:
            result = result.next
            start = start.next.next
        return result