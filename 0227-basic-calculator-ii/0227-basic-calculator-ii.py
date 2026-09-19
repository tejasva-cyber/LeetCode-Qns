class Solution(object):
    def calculate(self, s):
        stack = []
        current_num = 0
        operator = '+'
        
        for i, char in enumerate(s):
            # 1. Byte-level parsing instead of high-level string casting
            if '0' <= char <= '9':
                current_num = (current_num * 10) + (ord(char) - ord('0'))
                
            # 2. Trigger on specific operational bytes or End of File (EOF)
            if char in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(current_num)
                elif operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    stack[-1] = stack[-1] * current_num
                elif operator == '/':
                    # 3. Secure C-style truncation towards zero
                    prev = stack[-1]
                    if prev < 0:
                        stack[-1] = -(-prev // current_num)
                    else:
                        stack[-1] = prev // current_num
                        
                operator = char
                current_num = 0
                
        return sum(stack)