#!/usr/bin/python3
import argparse, operator

def xorbytes(a,b):
	if type(a) == bytearray:
		if type(b) == bytes:
			return bytearray(i ^ j for (i,j) in zip(a,bytearray(b)))
		elif type(b) == bytearray:
			return bytearray(i ^ j for (i,j) in zip(a,b))
		else:
			return bytearray(i ^ j for (i,j) in zip(a,bytearray.fromhex(b)))
	elif type(a) == bytes:
		if type(b) == bytes:
			return bytearray(i ^ j for (i,j) in zip(bytearray(a),bytearray(b)))
		elif type(b) == bytearray:
			return bytearray(i ^ j for (i,j) in zip(bytearray(a),b))
		else:
			return bytearray(i ^ j for (i,j) in zip(bytearray(a),bytearray.fromhex(b)))
	else:
		if type(b) == bytes:
			return bytearray(i ^ j for (i,j) in zip(bytearray.fromhex(a),bytearray(b)))
		elif type(b) == bytearray:
			return bytearray(i ^ j for (i,j) in zip(bytearray.fromhex(a),b))
		else:
			return bytearray(i ^ j for (i,j) in zip(bytearray.fromhex(a),bytearray.fromhex(b)))

def breaksinglexor(ciphertext,lang='eng',top=5):
	languages = {	'eng' : " etaoinshrdlucmfwypvbgkjqxz",
					'fra' : [],
					'esp' : [],
					'deu' : [],
					'por' : []}
	freq = dict()
	for key in range(256):
		plaintext = xorbytes(ciphertext,bytearray([key]*int(len(ciphertext)/2)).hex())
		try:
			strplaintext = plaintext.decode('utf-8')
		except UnicodeDecodeError:
			continue
		count = 0
		multiplicator = len(languages[lang])
		for letter in languages[lang]:
			count += strplaintext.count(letter) * multiplicator
			multiplicator -= 1
		freq[bytes([key]).hex()] = count
	sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
	ret = list()
	for i in sorted_freq[:top]:
		ret.append({'key' : i[0], 'plaintext' : xorbytes(ciphertext,i[0]*int(len(ciphertext)/2)).decode('utf-8'), 'count' : i[1]})
	return ret

if __name__ == "__main__":
	DESCRIPTION = """Break a ciphertext XOR'd with a single character.
	https://cryptopals.com/sets/1/challenges/3"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 3', description=DESCRIPTION)
	parser.add_argument('-c','--ciphertext', required=True, help='Ciphertext in hex string.')
	parser.add_argument('-l','--language', required=False, default='eng', choices=['eng', 'esp', 'deu', 'fra', 'por'], help='Language.')
	parser.add_argument('-t','--top', required=False, default=5, type=int, help='How many possible attempts to show.')
	args = parser.parse_args()
	print("Ciphertext: {0}".format(args.ciphertext))
	result = breaksinglexor(args.ciphertext,lang=args.language,top=args.top)
	print("Showing top {0} possible results:".format(str(args.top)))
	for i in result:
		print("Key: {0} Plaintext: {1}".format(i['key'],i['plaintext']))