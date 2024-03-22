import bluetooth
'''
pip install doesn't work, workaround:
To install package:
pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
'''
"""
End goal:
Emulate PS5 controller to console
Send inputs to console
"""


def list_available_devices():
    # List nearby detected bluetooth connections with addresses and readable names
    nearby_devices = bluetooth.discover_devices()

    if not nearby_devices:
        print("No Bluetooth devices found.")
        return

    # print("Available Bluetooth devices:")
    # for device in nearby_devices:
    #     print(device, bluetooth.lookup_name(device, timeout=8))
    return nearby_devices


def select_device(devices):
    counter = 1
    print("Found devices:")
    for device in devices:
        print(f"{counter}) {device} - {bluetooth.lookup_name(device, timeout=8)}")
        counter += 1
    choice = int(input("Select device to connect to [num]: "))
    return devices[choice-1]


def connect_to_device(address):
    # Connect to selected device
    try:
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        port = 1  # Port number for HID profile
        socket.connect((address, port))
        print(f"Successfully connected to {address}.")
        # Add something to do
        socket.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    device_list = list_available_devices()
    selection = select_device(device_list)
    # connect_to_device()
