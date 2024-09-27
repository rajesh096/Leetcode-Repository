class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_bookings:
            if max(start, s) < min(end, e):  
                return False

       
        for s, e in self.events:
            if max(start, s) < min(end, e):  
                self.double_bookings.append((max(start, s), min(end, e)))

        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)