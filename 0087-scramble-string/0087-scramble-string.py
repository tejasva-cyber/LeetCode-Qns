class Solution(object):
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
            
        # Initialize manual memoization dictionary
        memo = {}
        
        def dfs(a, b):
            state = (a, b)
            if state in memo:
                return memo[state]
                
            if a == b:
                memo[state] = True
                return True
                
            # Quick frequency validation to prune dead branches instantly
            if sorted(a) != sorted(b):
                memo[state] = False
                return False
                
            n = len(a)
            for i in range(1, n):
                # Path 1: Unswapped match attempt
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[state] = True
                    return True
                    
                # Path 2: Swapped match attempt (using Python negative indexing)
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[state] = True
                    return True
                    
            memo[state] = False
            return False
            
        return dfs(s1, s2)