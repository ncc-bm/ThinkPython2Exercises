class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print(time.hour)

Time.print_time(time)
time.print_time()