class Solution(object):
    def divide(self, dividend, divisor):
        # 1. Explicitly trap the integer overflow edge case immediately.
        # In 32-bit architectures, -2147483648 / -1 causes a hardware overflow exception.
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        # 2. Determine sign using inequality (cleaner and safer than XOR on booleans)
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        
        a, b = abs(dividend), abs(divisor)
        result = 0
        
        # 3. Bitwise shifting logic
        while a >= b:
            temp = b
            multiple = 1
            
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            a -= temp
            result += multiple
            
        return result if sign == 1 else -result