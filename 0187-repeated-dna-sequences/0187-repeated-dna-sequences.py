class Solution(object):
    def findRepeatedDnaSequences(self, s):
        # Hash sets provide O(1) lookup time
        seen = set()
        repeated = set()
        
        # A valid sequence must be exactly 10 characters long.
        # We iterate up to len(s) - 9 to prevent Index Out of Bounds errors.
        for i in range(len(s) - 9):
            # Extract the 10-byte sliding window
            dna_chunk = s[i:i + 10]
            
            if dna_chunk in seen:
                repeated.add(dna_chunk)
            else:
                seen.add(dna_chunk)
                
        # Cast the set back to a list to match LeetCode's expected return type
        return list(repeated)