#!/usr/bin/python3
import argparse, os, base64, challenge7

if __name__ == "__main__":
	DESCRIPTION = """Decrypt a base64 encoded file using AES-128-CBC mode.
	https://cryptopals.com/sets/2/challenges/10"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 2 - Challenge 10', description=DESCRIPTION)
	parser.add_argument('-f','--file', required=True, type=argparse.FileType('r') , help='File containing base64 encrypted data.')
	parser.add_argument('-k','--key', required=True, help='Key')
	args = parser.parse_args()
	data = base64.b64decode(args.file.read())
	print("Loaded {0} bytes of data.".format(os.path.getsize(args.file.name)))
	cipher = challenge7.AESCipher(bytes(args.key,'utf-8'))
	print("Decrypted message: {0}".format(cipher.decrypt(data,mode='CBC').decode('utf-8')))