#!/usr/bin/python3
import argparse, operator, os, base64, challenge3

def hamming_distance(s1, s2):
	if type(s1) != bytes:
		s1 = bytes(s1,'utf-8')
	if type(s2) != bytes:
		s2 = bytes(s2,'utf-8')
	count = 0
	for i in challenge3.xorbytes(s1.hex(),s2.hex()):
		if i&1:
			count += 1
		if i&2:
			count += 1
		if i&4:
			count += 1
		if i&8:
			count += 1
		if i&16:
			count += 1
		if i&32:
			count += 1
		if i&64:
			count += 1
		if i&128:
			count += 1
	return count

def probable_length(data,minlength=2,maxlength=40):
	assert type(data) == bytes
	possible_length = {'length' : minlength, 'distance' : 8*maxlength}
	chunks = lambda l, n: [l[x: x+n] for x in range(0, len(l), n)]
	for l in range(minlength,maxlength+1):
		chunked_data = chunks(data,l)
		suma = sum([hamming_distance(x,y) for x,y in zip(chunked_data[0::2], chunked_data[1::2])]) / (l*len(chunked_data))
		if possible_length['distance'] > suma:
			possible_length['distance'] = suma
			possible_length['length'] = l
	return possible_length['length']

def transpose(data):
	ret = list()
	for i in range(len(data[0])):
		ret.append(b''.join([bytes([x[i]]) for x in data[:-1]]))
	for i in data[-1]:
		ret[data[-1].index(i)] += bytes([i])
	return ret

def xorrepeatingkey(data,key):
	return challenge3.xorbytes(data,bytearray(((len(data)//len(key)+1)*key)[:len(data)]))

if __name__ == "__main__":
	DESCRIPTION = """There's a base64 encoded file which has been encrypted with a repeating XOR key, this script should break it.
	https://cryptopals.com/sets/1/challenges/6"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 6', description=DESCRIPTION)
	parser.add_argument('-f','--file', required=True, type=argparse.FileType('r') , help='File containing base64 encrypted data.')
	parser.add_argument('-m','--minkeylength', required=False, default=2, type=int, help='Minimum key length.')
	parser.add_argument('-M','--maxkeylength', required=False, default= 40, type=int, help='Maximum key length.')
	args = parser.parse_args()
	print("Loaded {0} bytes of data.".format(os.path.getsize(args.file.name)))
	data = base64.b64decode(args.file.read())
	args.file.close()
	length = probable_length(data,args.minkeylength,args.maxkeylength)
	print("Possible length: {0}".format(length))
	chunks = lambda l, n: [l[x: x+n] for x in range(0, len(l), n)]
	transposed_data = transpose(chunks(data,length))
	key = list()
	for a in transposed_data:
		key.append(challenge3.breaksinglexor(a.hex(),top=1)[0]['key'])
	key = bytearray.fromhex(''.join(key))
	print("The key is: {0}".format(key.decode('utf-8')))
	print("The plaintext is: {0}".format(xorrepeatingkey(data,key).decode('utf-8')))