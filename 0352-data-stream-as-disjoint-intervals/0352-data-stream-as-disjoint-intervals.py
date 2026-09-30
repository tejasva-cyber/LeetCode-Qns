class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value):
        self.nums.add(value)

    def getIntervals(self):
        if not self.nums:
            return []

        nums = sorted(self.nums)
        result = []

        start = prev = nums[0]

        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            else:
                result.append([start, prev])
                start = prev = num

        result.append([start, prev])

        return result