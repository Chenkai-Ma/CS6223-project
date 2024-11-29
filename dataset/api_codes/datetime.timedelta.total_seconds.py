def total_seconds(self):
        return ((self.days * 86400 + self.seconds) * 10**6 +
                self.microseconds) / 10**6