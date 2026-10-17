class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        radius = 0
        j = 0

        for house in houses:
            while j + 1 < len(heaters) and abs(heaters[j + 1] - house) <= abs(heaters[j] - house):
                j += 1

            radius = max(radius, abs(heaters[j] - house))

        return radius