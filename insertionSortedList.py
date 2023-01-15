class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        createdNode = ListNode(0)
        currentNode = head

        while currentNode:
            prev = createdNode
            while prev.next and prev.next.val < currentNode.val:
                prev = prev.next
            next = currentNode.next
            currentNode.next = prev.next
            prev.next = currentNode
            currentNode = next
        return createdNode.next