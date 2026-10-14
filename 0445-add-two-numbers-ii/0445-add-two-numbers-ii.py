class Solution:
    def addTwoNumbers(self, l1, l2):
        a, b = [], []

        while l1:
            a.append(l1.val)
            l1 = l1.next

        while l2:
            b.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while a or b or carry:
            total = (a.pop() if a else 0) + (b.pop() if b else 0) + carry
            carry = total // 10

            node = ListNode(total % 10)
            node.next = head
            head = node

        return head