#!/usr/bin/env python3

import argparse
import serial


class Relay:
	def __init__(self, path):
		self.relay = serial.Serial(path, 9600)
	def __del__(self):
		self.relay.close()
	def on(self):
		on_cmd = b'\xA0\x01\x01\xa2'
		self.relay.write(on_cmd)
	def off(self):
		off_cmd = b'\xA0\x01\x00\xa1'
		self.relay.write(off_cmd)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("path", type=str, help="Path to the relay (ex: /dev/ttyUSB0")
	parser.add_argument("--on", action="store_true", help="Turn the relay ON")
	parser.add_argument("--off", action="store_true", help="Turn the relay OFF")
	args = parser.parse_args()


	relay = Relay(args.path)
	if (args.on):
		relay.on()
	elif (args.off):
		relay.off()
