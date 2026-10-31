class Solution(object):
    def outerTrees(self, trees):
        # Base state: A perimeter of 3 or fewer nodes is already its own boundary
        if len(trees) <= 3:
            return trees

        # 1. O(N log N) Geometric Sweep Line: Sort nodes by X, then Y coordinate
        trees.sort(key=lambda p: (p[0], p[1]))

        # 2. Vector Math: 2D Cross Product to determine turn direction
        # If the result is negative, it's a right (clockwise) turn, meaning the 
        # previous node is an internal node and must be purged from the perimeter.
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # 3. Assemble the Lower Perimeter
        lower = []
        for t in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], t) < 0:
                lower.pop()
            lower.append(t)

        # 4. Assemble the Upper Perimeter (Scanning in reverse)
        upper = []
        for t in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], t) < 0:
                upper.pop()
            upper.append(t)

        # 5. Cryptographic Deduplication: Splice halves and use a Set to eliminate overlap
        hull = set(tuple(p) for p in (lower[:-1] + upper[:-1]))
        
        # Re-encode to the expected nested list format
        return [list(p) for p in hull]