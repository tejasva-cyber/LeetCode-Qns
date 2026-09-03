class Solution(object):
    def isNumber(self, s):
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ('+', '-'):
                # Signs are only allowed at the very beginning or immediately after an exponent
                if i > 0 and s[i-1] not in ('e', 'E'):
                    return False
            elif char in ('e', 'E'):
                # Exponents cannot appear twice, and MUST be preceded by a digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit because we MUST have a digit after the 'e'
                seen_digit = False
            elif char == '.':
                # Decimals cannot appear after an exponent or another decimal
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                # Any other character (letters, spaces, special chars) is instantly invalid
                return False
                
        # The string is only valid if it terminates having fulfilled the requirement for a final digit
        return seen_digit