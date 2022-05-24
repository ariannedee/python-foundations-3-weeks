class Clock:
    """24-hour clock showing the hour and minute"""

    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add(self, hours=0, minutes=0):
        extra_hours = (self.minutes + minutes) // 60
        self.minutes = (self.minutes + minutes) % 60
        self.hours = (self.hours + hours + extra_hours) % 24

    def __str__(self):
        hour_str = str(self.hours).zfill(2)
        min_str = str(self.minutes).zfill(2)
        return f'{hour_str}:{min_str}'

    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes})"
