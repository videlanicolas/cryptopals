#!/usr/bin/python3
import argparse, os, base64, random, challenge7
from collections import Counter

def randomAESkey(length=16):
	assert length in [16,24,32]
	return open("/dev/urandom","rb").read(length)

def generateciphertext(plaintext,length=16):
	assert length in [16,24,32]
	cipher = challenge7.AESCipher(randomAESkey(length))
	plaintext = open("/dev/urandom","rb").read(random.randint(5,10)) + plaintext + open("/dev/urandom","rb").read(random.randint(5,10))
	if random.randint(0,1):
		return (cipher.encrypt(cipher.pad(plaintext),mode='ECB'),'ECB')
	else:
		return (cipher.encrypt(cipher.pad(plaintext),mode='CBC',iv=randomAESkey(length)),'CBC')

def isECB(data,length=16):
	count = list()
	chunks = lambda l, n: [l[x: x+n] for x in range(0, len(l), n)]
	aux = 0
	if len(data)%16 == 0 or len(data)%24 == 0 or len(data)%32 == 0:
		d = chunks(data,length)
		for v in Counter(d).values():
			if v > 1:
				aux += v
	return True if aux else False

if __name__ == "__main__":
	DESCRIPTION = """Generate CBC and ECB encrypted messages and detect which one is happening.
	https://cryptopals.com/sets/2/challenges/11"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 2 - Challenge 11', description=DESCRIPTION)
	parser.add_argument('-s','--show-guess', required=False, action='store_true', default=False, help='Should the script show it\'s guesses?')
	parser.add_argument('-i','--input', required=True, help='Some input to be encrypted/decrypted')
	parser.add_argument('-a','--amount', required=False, default=40, type=int, help='Amount of ciphertexts to produce')
	args = parser.parse_args()
	plaintext = args.input
	print("Plaintext: {0}".format(plaintext))
	print("Generating {0} amount of ciphertexts ...".format(args.amount))
	ciphertexts = list()
	failed = 0
	matched = 0
	for i in range(args.amount):
		ciphertext, mode = generateciphertext(bytes(plaintext,'utf-8'))
		if isECB(ciphertext):
			if mode == 'ECB':
				if args.show_guess:
					print("Matched! (ECB).")
				matched += 1
			else:
				if args.show_guess:
					print("Failed! Said ECB and was CBC.")
				failed += 1
		else:
			if mode == 'CBC':
				if args.show_guess:
					print("Matched! (CBC).")
				matched += 1
			else:
				if args.show_guess:
					print("Failed! Said CBC and was ECB.")
				failed += 1
		if args.show_guess:
			print("##############")
	print("Results: Matched = {:.2f}% Failed = {:.2f}%".format(100.0*matched/(matched + failed),100.0*failed/(matched + failed)))