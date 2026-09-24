class Solution(object):
    def removeInvalidParentheses(self, s):
        # 1. State Validation Engine
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # Level 0: The original payload
        current_level = {s}
        
        while True:
            # 2. Parallel scan of the current network layer
            valid_payloads = [x for x in current_level if is_valid(x)]
            
            # 3. If valid configurations exist at this depth, terminate execution
            if valid_payloads:
                return valid_payloads
                
            # 4. Generate the next layer of permutations (1 additional removal)
            next_level = set()
            for string in current_level:
                for i in range(len(string)):
                    # Only mutate if the character is a bracket
                    if string[i] in '()':
                        # Zero-copy slice: stitch the left and right halves together
                        mutated_string = string[:i] + string[i+1:]
                        # The set() architecture instantly drops identical mutations
                        next_level.add(mutated_string)
                        
            # Advance the scanner to the next depth
            current_level = next_level