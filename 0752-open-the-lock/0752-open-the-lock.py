class Solution:
    def openLock(self, deadends, target):
        from collections import deque

        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            state, steps = queue.popleft()

            for i in range(4):
                digit = int(state[i])

                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    nxt = state[:i] + str(new_digit) + state[i + 1:]

                    if nxt == target:
                        return steps + 1

                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))

        return -1