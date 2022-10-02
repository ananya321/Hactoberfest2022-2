#https://leetcode.com/problems/linked-list-cycle/
def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow :
                return True
        return False
