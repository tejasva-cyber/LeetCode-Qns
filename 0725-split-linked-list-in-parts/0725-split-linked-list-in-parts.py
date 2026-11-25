class Solution:
    def splitListToParts(self, head, k):
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        base, extra = divmod(length, k)
        result = []
        current = head

        for i in range(k):
            part = current
            size = base + (1 if i < extra else 0)

            for _ in range(size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

            result.append(part)

        return result