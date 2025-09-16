class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length=1
        dummy=head
        while dummy.next:
            dummy=dummy.next
            length+=1
        position=k%length
        if position==0:
            return head
        cur=head
        for i in range(length-position-1):
            cur=cur.next

        newhead=cur.next
        cur.next=None
        dummy.next=head
        return newhead