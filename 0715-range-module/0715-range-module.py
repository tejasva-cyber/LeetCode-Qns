class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        result = []
        for start, end in self.intervals:
            if end < left:
                result.append([start, end])
            elif right < start:
                result.append([left, right])
                left, right = start, end
            else:
                left = min(left, start)
                right = max(right, end)

        result.append([left, right])
        self.intervals = result

    def queryRange(self, left, right):
        return any(
            start <= left and right <= end
            for start, end in self.intervals
        )

    def removeRange(self, left, right):
        result = []

        for start, end in self.intervals:
            if end <= left or start >= right:
                result.append([start, end])
            else:
                if start < left:
                    result.append([start, left])
                if end > right:
                    result.append([right, end])

        self.intervals = result