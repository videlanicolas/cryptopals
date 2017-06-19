#!/usr/bin/python3
import argparse

def xorbytes(a,b):
	return bytearray(i ^ j for (i,j) in zip(bytearray.fromhex(a),bytearray.fromhex(b)))

if __name__ == "__main__":
	DESCRIPTION = """Take two bytes encoded as Hex A and B, return the XOR of both bytes.
	https://cryptopals.com/sets/1/challenges/2"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 2', description=DESCRIPTION)
	parser.add_argument('-a', required=True, help='Hex byte string A.')
	parser.add_argument('-b', required=True, help='Hex byte string B.')
	args = parser.parse_args()
	print("A: {0}".format(args.a))
	print("A (UTF-8): {0}".format(bytearray.fromhex(args.a).decode('utf-8')))
	print("B: {0}".format(args.b))
	print("B (UTF-8): {0}".format(bytearray.fromhex(args.b).decode('utf-8')))
	print("A ^ B: {0}".format(xorbytes(args.a,args.b).hex()))
	print("A ^ B (UTF-8): {0}".format(xorbytes(args.a,args.b).decode('utf-8')))