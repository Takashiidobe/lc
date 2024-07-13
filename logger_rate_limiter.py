# @leet start
class Logger:
    """
    This logger class implements a logger that debounces logging calls.
    The first time the logger sees a message, it decides to log it, and count for 10 seconds
    since it last saw that message.
    If it has seen the message within 10 seconds, it doesn't log the message.

    To keep track of everything, we can create a dictionary that maps key -> last logged timestamp.
    Then, when a new message comes along, if it either doesn't exist in the dictionary or
    it hasn't been logged for at least 10 seconds, we set the message's new timestamp and log the message.
    Otherwise, no logging is done.
    """
    def __init__(self):
        self.times = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.times or self.times[message] + 10 <= timestamp:
            self.times[message] = timestamp
            return True
        else:
            return False

def test():
	assert(2 + 2 == 4)
