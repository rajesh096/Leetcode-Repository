class MyCalendar:
    def __init__(self):
        # Initialize an empty list to store the events
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlaps with existing events
        for s, e in self.events:
            # If there's an overlap, return False
            if max(start, s) < min(end, e):
                return False
        
        # If no overlap, add the event and return True
        self.events.append((start, end))
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)