class Solution(object):
    def isValid(self, code):
        stack = []
        i = 0
        n = len(code)

        while i < n:
            # Enforce single root node: if we are mid-string and the stack is empty, it's invalid.
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                # CDATA cannot exist outside the root tag
                if not stack:
                    return False
                j = code.find("]]>", i + 9)
                if j == -1:
                    return False
                i = j + 3

            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i + 2:j]
                if not stack or stack[-1] != tag:
                    return False

                stack.pop()
                i = j + 1

            elif code.startswith("<", i):
                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i + 1:j]
                
                # Deterministic Byte Validation: Replaces the flawed .isupper()
                if not tag or len(tag) > 9 or not all('A' <= c <= 'Z' for c in tag):
                    return False

                stack.append(tag)
                i = j + 1

            else:
                if not stack:
                    return False
                i += 1

        return not stack and code.startswith("<")