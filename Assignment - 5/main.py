from device import Device
from smartphone import Smartphone


if __name__ == '__main__':
    device = Device('Dname', 534,20, '2344' )
    print(device.is_available(20))
    print(device.is_available(25))

    smartphone = Smartphone('IPhone', 1000, 100, '2025', 6, 8)
    print(smartphone)

