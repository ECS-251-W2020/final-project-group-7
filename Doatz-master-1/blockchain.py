import hashlib
import json
from time import time
from datetime import datetime
#from time import clock
from urllib.parse import urlparse
from uuid import uuid4

import requests
import socket
from flask import Flask, jsonify, request
from flask import render_template

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        self.port = "5000"
        self.password = ""
        self.keylist = set()
        self.candidate_list = set()
        self.intro = ""
        self.candidate = []
        #self.voteInfo = {}

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def register_node(self, address):
        """
        Add a new node to the list of nodes

        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid

        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.

        :return: True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        if sender == "0":
            amount = 1
        elif sender not in self.keylist:
            amount = 0
        elif recipient not in self.candidate_list:
            amount = 0
        else:
            amount = 1
            self.keylist.remove(sender)

        """
        Creates a new transaction to go into the next mined Block

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timeStamp': str(time())
        })

        return self.last_block['index'] + 1
    
    def createCryptoKey(self, email):
        return str(uuid4()).replace('-', '')[-16:]
    
    def get_host_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip

    def sendAttenderEmail(self, emailList, port):
        host_server = 'smtp.qq.com'
        sender_qq = '1713363421'
        pwd = 'choooqcngrlyfbbg'
        sender_qq_mail = '1713363421@qq.com'
        
        smtp = SMTP_SSL(host_server)
        smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)
        
        mail_title = 'An invitation to vote'
        mail_localIP = self.get_host_ip()
        
        for email in emailList:
            key = self.createCryptoKey(email)
            #self.keylist[email] = key
            self.keylist.add(key)
            mail_content = 'Dear attender, here is an invitation to participate in an interesting vote. \
            The website is http://'+ mail_localIP + ':5000, and the port number is ' + str(port) + ' , and your crypto key is ' + str(key) + '\
                 And you can check the voting progress anytime at ' + mail_localIP + ':' + str(port) + '/chainDetail'


            receiver = email
            msg = MIMEText(mail_content, "plain", 'utf-8')
            msg["Subject"] = Header(mail_title, 'utf-8')
            msg["From"] = sender_qq_mail
            msg["To"] = receiver
            smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        
        smtp.quit()
        return

    def countVote(self):
        vote_result = {}

        #candidate_block = self.chain[1]
        #candidate_transaction = candidate_block['transactions'][1]

        #already_vote_keylist = set()

        for candidate in self.candidate_list:
            vote_result[candidate] = 0

        #print(vote_result)

        for i in range(0, len(self.chain)):
            block = self.chain[i]
            for transaction in block['transactions']:
                if 'sender' not in transaction or 'recipient' not in transaction or 'amount' not in transaction:
                    continue

                sender = transaction['sender']
                recipient = transaction['recipient']
                amount = transaction['amount']
                if sender == "0" or amount == 0:
                    continue
                #if sender not in self.keylist:                            #not valid participant
                    #continue
                #elif sender in already_vote_keylist:                      #participant already vote
                    #continue
                #elif recipient not in vote_result:                        #not valid candidate
                    #continue
                else:
                    vote_result[recipient] = vote_result[recipient] + 1
                    #already_vote_keylist.add(sender)

        print(vote_result)
        return vote_result



    def printVote(self):
        bollats = []
        vote_result = {}
        
        for candidate in self.candidate_list:
            vote_result[candidate] = 0

        for i in range(0, len(self.chain)):
            block = self.chain[i]
            for transaction in block['transactions']:
                if 'sender' not in transaction or 'recipient' not in transaction or 'amount' not in transaction:
                    continue

                sender = transaction['sender']
                recipient = transaction['recipient']
                amount = transaction['amount']
                time = transaction['timeStamp']

                if sender == "0" :
                    continue
                else :
                    if amount == 0 :
                        newBallot = {
                            "sender" : sender,
                            "candidate" : recipient,
                            "verified" : False,
                            "time" : time
                        }
                        bollats.append(newBallot)
                        continue
                    else:
                        newBallot = {
                            "sender" : sender,
                            "candidate" : recipient,
                            "verified" : True,
                            "time" : time
                        }
                        bollats.append(newBallot)
                        vote_result[recipient] = vote_result[recipient] + 1
                        #already_vote_keylist.add(sender)

        vote_result["leftVotes"] = len(self.keylist)

        vote_detail = {
            "voteName": self.intro,
            "candidate": self.candidate,
            "ballots":bollats,
            "voteResult": vote_result
        }

        print(vote_detail)
        return vote_detail


    def setVoteInitInfo(self, voteInfo):
        #Init the Voting info
        #1 add intro & candidate into block
        self.current_transactions.append(voteInfo.get('voteIntro'))
        self.current_transactions.append(voteInfo.get('candidate'))

        self.intro = voteInfo.get('voteIntro')
        self.candidate = voteInfo.get('candidate')
        for candidate in self.candidate:
            self.candidate_list.add(candidate)

        #2 send email to all attender (with cryptokey) and save the list of key
        self.sendAttenderEmail(voteInfo.get('emailList'),voteInfo.get('port'))


    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof
         
        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)
        
        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        #print(proof)

        return proof

    @staticmethod
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
        return guess_hash[:4] == "0000"

    


# Instantiate the Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block

    #time_start=clock()
    
    proof = blockchain.proof_of_work(last_block)
    
    #time_end=clock()
    #print('time cost:',time_end-time_start)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@app.route('/chainDetail', methods=['GET'])
def votingDetail():
    response = blockchain.printVote()
    #return jsonify(response), 200
    return render_template('chainDetail.html', content = response)


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


@app.route('/initVote', methods=['POST'])
def initVoteMessage():
    values = request.get_json()

    required = ['timestamp', 'voteIntro', 'candidate', 'emailList', 'startTime', 'endTime', 'port', 'password']
    # mayby deal with Possible fields like 'voteName', 'briefIntro' later...

    if not all(k in values for k in required):
        return 'Missing values', 400
    
    if blockchain.port != values.get('port'):
        return "Port Error: Send to the wrong port", 400

    if blockchain.password != values.get('password'):
        return "Error: Your password does not fit to this chain", 401

    print(values)

    blockchain.setVoteInitInfo(values)

    #for node in nodes:
    #   blockchain.register_node(node)

    response = {
        'message': 'Vote Chain Created Successfully',
        #'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/voteTimeEnd', methods=['POST'])
def votingTimeEnd():
    values = request.get_json()

    required = ['password']

    if not all(k in values for k in required):
        return 'Missing values', 400
    
    if blockchain.password != values.get('password'):
        return "Error: Your password does not fit to this chain", 401
    
    #here, call the function countVote() print the result
    return jsonify(blockchain.countVote()), 203


@app.route('/DeleteChain', methods=['POST'])
def DeleteChain():
    values = request.get_json()
    required = ['password','port']
    if not all(k in values for k in required):
        print('Missing values', 400)
        return 'Missing values', 400
    if blockchain.port != values.get('port'):
        print("Port Error: Send to the wrong port")
        return "Port Error: Send to the wrong port", 400
    if blockchain.password != values.get('password'):
        return "Error: Your password does not fit to this chain", 401
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    with open(blockchain.port + "record.json","w") as f:
        json.dump(response,f)
    return jsonify(response), 204

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    parser.add_argument('-k', '--key', default='votingKey', type=str, help='controling Password')
    args = parser.parse_args()
    blockchain.port = str(args.port)
    blockchain.password = args.key

    print("=============NEW CHAIN CREAT============")
    print("port: ",blockchain.port)
    print("password: ",blockchain.password)

    app.run(host='0.0.0.0', port=blockchain.port)
