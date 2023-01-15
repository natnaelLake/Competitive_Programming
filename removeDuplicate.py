class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        createdNode = ListNode(0, head)
        prevNode = createdNode
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prevNode.next == head:
                prevNode = prevNode.next
            else:
                prevNode.next = head.next
            head = head.next
        return createdNode.next