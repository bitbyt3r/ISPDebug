import usbtinyisp
import time
import bitstring

tiny = usbtinyisp.usbtiny()
tiny.power_on()

ROT = [0xAA, 0x55, 0x2A, 0x15, 0x0A, 0x05, 0x02, 0x01]

while True:
    data = tiny.spi1(0)[0]
    if data == 0:
        continue
    if not data in ROT:
        continue
    rot = ROT.index(data) # rot is the number of bit positions we are out of sync.
    string = bytearray([data])
    while data != 0:
        data = tiny.spi1(0)[0]
        string.append(data)
    bits = bitstring.BitArray(bytes=string) << rot
    raw = bits.tobytes()
    while raw.startswith(bytes([0xAA])):
        raw = raw[1:]
    while raw.endswith(bytes([0x00])):
        raw = raw[:-1]
    try:
        print(raw.decode('ASCII'), end="")
    except UnicodeDecodeError:
        print(raw)