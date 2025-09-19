class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd,even=head,head.next
        even_head=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return head
