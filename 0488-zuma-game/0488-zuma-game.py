import collections

class Solution(object):
    def findMinStep(self, board, hand):
        # 1. Deterministic memory cleanup function
        def clean(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    s = s[:i] + s[j:]
                    i = 0 
                else:
                    i += 1
            return s
            
        # 2. Immutable state serialization
        hand = "".join(sorted(hand))
        queue = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])
        
        while queue:
            b, h, steps = queue.popleft()
            
            if not b:
                return steps
                
            # 3. Active Threat Mapping (BFS Level Generation)
            for i in range(len(b) + 1):
                for j in range(len(h)):
                    # Deduplicate identical ammo payloads
                    if j > 0 and h[j] == h[j-1]:
                        continue
                        
                    ball = h[j]
                    
                    # Execution Pruning: Only branch if it advances the state
                    match_curr = i < len(b) and b[i] == ball
                    match_bridge = i > 0 and i < len(b) and b[i-1] == b[i] and b[i] != ball
                    
                    if match_curr or match_bridge:
                        nb = clean(b[:i] + ball + b[i:])
                        nh = h[:j] + h[j+1:]
                        
                        if (nb, nh) not in visited:
                            visited.add((nb, nh))
                            queue.append((nb, nh, steps + 1))
                            
        return -1