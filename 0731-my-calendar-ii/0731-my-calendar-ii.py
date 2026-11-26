class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        for left, right in self.overlaps:
            if start < right and left < end:
                return False

        for left, right in self.bookings:
            if start < right and left < end:
                self.overlaps.append((max(start, left), min(end, right)))

        self.bookings.append((start, end))
        return True