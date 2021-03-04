

import sys
from time import sleep
sys.path.append('../python_base_classes')
print(sys.path)
from socket_control import socket_control


class system_upgrade_control(socket_control):
    def __init__(self, iAddr, iPort=5025):
        super().__init__(iAddr, iPort)


if __name__ == "__main__":
    test = socket_control('192.168.68.109', 5025)
    print(test.is_connected)

    try:
        test.connect()
        sleep(0.5)
        print(test.send_comm_layer('hello'))
        print(test.is_connected)
        sleep(1)

    finally:
        test.close()
        print(test.is_connected)



