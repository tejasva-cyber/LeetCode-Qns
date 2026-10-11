class Solution:
    def thirdMax(self, nums):
        top = set()

        for num in nums:
            top.add(num)
            if len(top) > 3:
                top.remove(min(top))

        return min(top) if len(top) == 3 else max(top)