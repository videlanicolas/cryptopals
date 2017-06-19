#!/usr/bin/python3
import argparse, challenge3

if __name__ == "__main__":
	DESCRIPTION = """Encrypt a string using repeating XOR byte.
	https://cryptopals.com/sets/1/challenges/5"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 5', description=DESCRIPTION)
	parser.add_argument('-f','--file', required=True, type=argparse.FileType('r') , help='File containing plaintext to encrypt.')
	parser.add_argument('-k','--key', required=True , help='Key to XOR the plaintext.')
	args = parser.parse_args()
	plaintext = args.file.read()
	print("Plaintext: {0}".format(plaintext))
	print("Key: {0}".format(args.key))
	result = challenge3.xorbytes(bytes(plaintext,'utf-8').hex(),bytes(((len(plaintext)//len(args.key)+1)*args.key)[:len(plaintext)],'utf-8').hex())
	print("Cipher: {0}".format(result.hex()))