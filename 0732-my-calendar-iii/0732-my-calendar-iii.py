from collections import defaultdict

class MyCalendarThree:

    def __init__(self):
        self.events = defaultdict(int)

    def book(self, startTime, endTime):
        self.events[startTime] += 1
        self.events[endTime] -= 1

        active = maximum = 0

        for time in sorted(self.events):
            active += self.events[time]
            maximum = max(maximum, active)

        return maximum