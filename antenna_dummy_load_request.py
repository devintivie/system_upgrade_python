from icd_message import *


class antenna_dummy_load_request(icd_message):
    def __init__(self):
        super().__init__()
        self.state = 'dummy_load'


if __name__ == "__main__":
    adr = antenna_dummy_load_request()
    print(adr.header.time)