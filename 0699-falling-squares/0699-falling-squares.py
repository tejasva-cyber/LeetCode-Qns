class Solution:
    def fallingSquares(self, positions):
        intervals = []
        result = []
        maximum = 0

        for left, side in positions:
            right = left + side
            height = side

            for old_left, old_right, old_height in intervals:
                if left < old_right and right > old_left:
                    height = max(height, old_height + side)

            intervals.append((left, right, height))
            maximum = max(maximum, height)
            result.append(maximum)

        return result