class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        Stack = []
        while head:
            while Stack and head.val > answer[Stack[-1]]:
                index = Stack.pop()
                answer[index] = head.val
            Stack.append(len(answer))
            answer.append(head.val)
            head = head.next
        for i in Stack:
            answer[i] = 0
        return answer