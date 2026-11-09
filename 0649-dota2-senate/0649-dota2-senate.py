import collections

class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        r_queue = collections.deque()
        d_queue = collections.deque()
        
        # 1. State Allocation: Map the exact temporal indices of the payload
        for i, char in enumerate(senate):
            if char == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        # 2. Execution Loop: Temporal offset banning
        while r_queue and d_queue:
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft()
            
            # The node with the earlier execution cycle terminates the opponent.
            # The victor is appended to the back of the queue for the next polling cycle.
            if r_idx < d_idx:
                r_queue.append(r_idx + n)
            else:
                d_queue.append(d_idx + n)
                
        # 3. State Resolution: The queue with surviving nodes wins
        return "Radiant" if r_queue else "Dire"