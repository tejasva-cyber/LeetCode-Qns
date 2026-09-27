class Solution(object):
    def oddEvenList(self, head):
        # Base case: If the list is empty or has only one node, no rewiring is needed
        if not head or not head.next:
            return head
            
        # Initialize execution pointers for two separate memory chains
        odd = head
        even = head.next
        
        # We must anchor the start of the even chain so we can splice it later
        even_head = even 
        
        # Traverse the structure, rewiring pointers sequentially
        while even and even.next:
            # Wire the current odd node to the next odd node (bypassing the even node)
            odd.next = even.next
            odd = odd.next
            
            # Wire the current even node to the next even node (bypassing the odd node)
            even.next = odd.next
            even = even.next
            
        # Splice the two independent chains back together
        odd.next = even_head
        
        return head