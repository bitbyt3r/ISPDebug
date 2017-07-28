# USBTinyAVR debug scope

A simple script to plot values form an AVR chip using the ISP header.

![example plot](example.png)

## Usage

Should work with any USBTinyAVR compatible programmer and any AVR chip that supports SPI slave on the ISP pins. Requires PyUSB, numpy and matplotlib.

An example Arduino script is provided to set up SPI correctly.

Simply run `python3 debug.py` and you should be good.

## Known issues

The ISP does not have a slave select pin. SS needs to be tied to ground.

If you get bogus data, try resetting the AVR and/or the debug script, the SPI has probably fallen out of sync.
