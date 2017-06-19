#!/usr/bin/python3
import argparse, base64

def hex2base64(hexstring):
	b = bytearray.fromhex(hexstring)
	return base64.b64encode(b).decode('utf-8')

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 1', description='https://cryptopals.com/sets/1/challenges/1')
	parser.add_argument('-s','--string',required=True, help='Hex string to be encoded to Base64.')
	args = parser.parse_args()
	print("Hex bytes: {0}".format(args.string))
	print("UTF-8 decoded bytes: {0}".format(bytearray.fromhex(args.string).decode('utf-8')))
	print("Base64 of decoded bytes: {0}".format(hex2base64(args.string)))