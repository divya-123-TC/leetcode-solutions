class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None

        left=self.sortList(head)
        right=self.sortList(mid)
        def merge(l1,l2):
            dummy=cur=ListNode(0)
            while l1 and l2:
                if l1.val<l2.val:
                    cur.next=l1
                    l1=l1.next
                else:
                    cur.next=l2
                    l2=l2.next
                cur=cur.next
            cur.next=l1 if l1 else l2
            return dummy.next
        return merge(left,right)