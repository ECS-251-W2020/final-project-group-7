import hashlib
import json
from time import time
from uuid import uuid4

def hash(block):
	"""
	Creates a SHA-256 hash of a Block

	:param block: Block
	"""

	# We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
	block_string = json.dumps(block, sort_keys=True).encode()
	return hashlib.sha256(block_string).hexdigest()

def proof_of_work(last_block):
	"""
	Simple Proof of Work Algorithm:

	 - Find a number p' such that hash(pp') contains leading 4 zeroes
	 - Where p is the previous proof, and p' is the new proof
	 
	:param last_block: <dict> last Block
	:return: <int>
	"""

	last_proof = last_block['proof']
	last_hash = hash(last_block)
	
	proof = 0
	while valid_proof(last_proof, proof, last_hash) is False:
		proof += 1

	#print(proof)

	return proof


def valid_proof(last_proof, proof, last_hash):
	"""
	Validates the Proof

	:param last_proof: <int> Previous Proof
	:param proof: <int> Current Proof
	:param last_hash: <str> The hash of the Previous Block
	:return: <bool> True if correct, False if not.

	"""

	guess = f'{last_proof}{proof}{last_hash}'.encode()
	guess_hash = hashlib.sha256(guess).hexdigest()
	return guess_hash[:1] == "0"

i = 0
proof = 0
previous_hash = 0

block = {
	'index': i,
	'timestamp': time(),
	'transactions': str(uuid4()).replace('-', '')[-16:],
	'proof': proof,
	'previous_hash': previous_hash or 0,
}

sss = 0
t1 = time()

while i < 100:
	i += 1
	t01 = time()
	proof = proof_of_work(block)
	t02 = time() - t01
	sss += t02
	print("========== block ",i," ==============")
	print("get proof ",proof," in ",t02)
	previous_hash = hash(block)
	block = {
		'index': i,
		'timestamp': time(),
		'transactions': str(uuid4()).replace('-', '')[-16:],
		'proof': proof,
		'previous_hash': previous_hash or 0,
	}

t2 = time()

print("****************************")
print("****************************")
print("finish 100 proof in ",t2-t1)
print("----------------------------")
print("pure proof time is ",sss)
