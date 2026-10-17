class Solution(object):
    def validIPAddress(self, queryIP):
        # 1. Branch Prediction based on structural delimiters
        if '.' in queryIP:
            # IPv4 Validation Protocol
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
                
            for part in parts:
                # Reject empty chunks or non-numeric bytes
                if not part or not part.isdigit():
                    return "Neither"
                # Reject leading zeros (Octal Evasion Trap)
                if part[0] == '0' and len(part) > 1:
                    return "Neither"
                # Validate byte boundaries (0-255)
                if int(part) > 255:
                    return "Neither"
            return "IPv4"
            
        elif ':' in queryIP:
            # IPv6 Validation Protocol
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
                
            # Hexadecimal validation map
            valid_hex = set("0123456789abcdefABCDEF")
            for part in parts:
                # Enforce strict 16-bit block sizes
                if not (1 <= len(part) <= 4):
                    return "Neither"
                for char in part:
                    if char not in valid_hex:
                        return "Neither"
            return "IPv6"
            
        return "Neither"