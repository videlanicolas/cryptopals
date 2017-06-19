#!/usr/bin/python3
import argparse, challenge3

if __name__ == "__main__":
	DESCRIPTION = """Find a single XOR'd ciphertext in a list of ciphertexts and break it.
	https://cryptopals.com/sets/1/challenges/4"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 4', description=DESCRIPTION)
	parser.add_argument('-f','--file', required=True, type=argparse.FileType('r') , help='File containing ciphertexts one per line.')
	args = parser.parse_args()
	ciphertexts = args.file.read().splitlines()
	print("{0} ciphertexts loaded.".format(len(ciphertexts)))
	result = list()
	for ciphertext in ciphertexts:
		result.append(challenge3.breaksinglexor(ciphertext,top=1))
	print("Showing possible result:")
	candidate = {'count' : 0}
	j = 0
	for i in result:
		if i:
			if candidate['count'] < i[0]['count']:
				candidate = i[0]
				j = result.index(i)
	print("Key: {0} Ciphertext: {1} Plaintext: {2}".format(candidate['key'],ciphertexts[j],candidate['plaintext']))