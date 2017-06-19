#!/usr/bin/python3
import argparse, operator

def xorbytes(a,b):
	return bytearray(i ^ j for (i,j) in zip(bytearray.fromhex(a),bytearray.fromhex(b)))

def breaksinglexor(ciphertext,lang='eng',top=5):
	languages = {	'eng' : ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us'], 
					'fra' : [],
					'esp' : [],
					'deu' : [],
					'por' : []}
	freq = dict()
	for key in range(256):
		plaintext = xorbytes(ciphertext,bytearray([key]*len(ciphertext)).hex())
		try:
			strplaintext = plaintext.decode('utf-8')
		except UnicodeDecodeError:
			continue
		count = 0
		multiplicator = 1
		for word in languages[lang]:
			count += strplaintext.count(word) * multiplicator
			multiplicator += 1
		freq[bytes([key]).hex()] = (count,plaintext)
	sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
	ret = list()
	for i in sorted_freq[:top]:
		ret.append({'key' : i[0], 'plaintext' : i[1][1].decode('utf-8')})
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