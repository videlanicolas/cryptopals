#!/usr/bin/python3
import argparse, os, challenge7
from Crypto.Cipher import AES

if __name__ == "__main__":
	DESCRIPTION = """Padd a string to PKCS #7 compliant format.
	https://cryptopals.com/sets/2/challenges/9"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 2 - Challenge 9', description=DESCRIPTION)
	parser.add_argument('-s','--string', required=True, help='String to be padded')
	parser.add_argument('-p','--pad', required=True, choices=[16,24,32], type=int, help='Length of block')
	args = parser.parse_args()
	print("String: {0}".format(args.string))
	cipher = challenge7.AESCipher(b'\x00'*args.pad)
	print("Padded string: {0}".format(cipher.pad(args.string)))