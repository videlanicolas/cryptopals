#!/usr/bin/python3
import argparse, os, challenge7, challenge6
from Crypto.Cipher import AES
from collections import Counter

if __name__ == "__main__":
	DESCRIPTION = """There's a file with a bunch of hex encoded strings and one of them is encrypted with AES-128-ECB, find which one is it.
	https://cryptopals.com/sets/1/challenges/8"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 8', description=DESCRIPTION)
	parser.add_argument('-f','--file', required=True, type=argparse.FileType('r') , help='File containing hex encoded strings.')
	args = parser.parse_args()
	data = args.file.read().splitlines()
	print("Loaded {0} bytes of data.".format(os.path.getsize(args.file.name)))
	count = list()
	chunks = lambda l, n: [l[x: x+n] for x in range(0, len(l), n)]
	for d in data:
		aux = 0
		if len(bytes.fromhex(d))%16 == 0:
			d = chunks(d,16)
			for v in Counter(d).values():
				if v > 1:
					aux += v
			count.append(aux)
		else:
			count.append(0)
	print("Possible AES-128-ECB encrypted strings are:")
	for i in [i for i, j in enumerate(count) if j == max(count)]:
		print(data[i])