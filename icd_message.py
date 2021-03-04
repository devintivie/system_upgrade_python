
from datetime import datetime


class icd_message:
    def __init__(self):
        self.header = icd_message_header()

class icd_message_header:
    def __init__(self, time = None):
        if time == None:
            self.time = datetime.now()
            print(self.time)
        else:
            self.time = time
        self.source = None
        self.destination = None

if __name__ == "__main__":
    msg = icd_message()
    print(msg.header.time)