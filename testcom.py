import bluetooth

port = 1

socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Device discovery
dev_list = bluetooth.discover_devices()
print("FOUND DEVICES")
for d in dev_list:
    print(d, "|", bluetooth.lookup_name(d))
print()

print("Connect to?", end=" ")
index = int(input()) - 1
print()

socket.connect((dev_list[index], port))
print("Connected to", dev_list[index], "on port", port)

socket.send("Hello world")

socket.close()
