#!/usr/bin/python3
import argparse, os, base64, challenge3
from Crypto.Cipher import AES

class AESCipher(object):
	def __init__(self,key=None):
		assert (key != None and len(key) in [16,24,32] and type(key) == bytes) or key == None
		self.key = key
		self.chunks = lambda l, n: [l[x: x+n] for x in range(0, len(l), n)]

	def __decrypt_single_block(self,block):
		assert type(block) == bytes and len(block) in [16,24,32]
		cipher = AES.new(self.key)
		return cipher.decrypt(block)

	def __encrypt_single_block(self,block):
		assert type(block) == bytes and len(block) in [16,24,32]
		cipher = AES.new(self.key)
		return cipher.encrypt(block)

	def pad(self,data,mode='pkcs7'):
		if type(data) != bytes:
			data = bytes(data,'utf-8')
		if mode == 'pkcs7':
			_data = self.chunks(data,len(self.key))[-1]
			if len(self.key) - len(_data) == 0:
				return data + bytes([len(self.key)])*len(self.key)
			else:
				return data + bytes([len(self.key) - len(_data)])*(len(self.key) - len(_data))

	def unpad(self,data,mode='pkcs7'):
		return data

	def encrypt(self,data,mode='ECB',iv=None):
		ret = list()
		if not iv:
			iv = b'\x00'*len(self.key)
		if mode == 'ECB':
			for block in self.chunks(data,len(self.key)):
				ret.append(self.__encrypt_single_block(block))
			return b''.join(ret)
		elif mode == 'CBC':
			for block in self.chunks(data,len(self.key)):
				iv = self.__encrypt_single_block(bytes(challenge3.xorbytes(block,iv)))
				ret.append(iv)
			return b''.join(ret)

	def decrypt(self,data,mode='ECB',iv=None):
		ret = list()
		if not iv:
			iv = b'\x00'*len(self.key)
		if mode == 'ECB':
			for block in self.chunks(data,len(self.key)):
				ret.append(self.__decrypt_single_block(block))
			return b''.join(ret)
		elif mode == 'CBC':
			for block in self.chunks(data,len(self.key)):
				ret.append(challenge3.xorbytes(self.__decrypt_single_block(block),iv))
				iv = block
			return b''.join(ret)


if __name__ == "__main__":
	DESCRIPTION = """There's a base64 encrypted file with AES-128-ECB under the key "YELLOW SUBMARINE", decrypt it.
	https://cryptopals.com/sets/1/challenges/7"""
	parser = argparse.ArgumentParser(prog='Cryptopals Set 1 - Challenge 7', description=DESCRIPTION)
	parser.add_argument('-f','--file', required=True, type=argparse.FileType('r') , help='File containing base64 encrypted data.')
	parser.add_argument('-k','--key', required=True, help='Key')
	args = parser.parse_args()
	data = base64.b64decode(args.file.read())
	print("Loaded {0} bytes of data.".format(os.path.getsize(args.file.name)))
	key = bytes(args.key,'utf-8')
	print("Key is {0}".format(args.key))
	cipher = AESCipher(key)
	decrypted = cipher.decrypt(data,mode='ECB')
	print("Decrypted text: {0}".format(decrypted.decode('utf-8')))