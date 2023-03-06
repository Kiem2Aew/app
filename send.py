import os
import sys
import glob
from bluetooth import *

# Specify the path of the file to be sent
file_path = '/path/to/file'

# Search for nearby Bluetooth devices
nearby_devices = discover_devices()

# Select the first device in the list (you can modify this based on your needs)
target_device = nearby_devices[0]

# Create a Bluetooth socket
sock = BluetoothSocket(RFCOMM)

# Connect to the target device
sock.connect((target_device, 1))

# Send the file to the target device
with open(file_path, 'rb') as f:
    data = f.read()
    sock.sendall(data)

# Close the socket
sock.close()
