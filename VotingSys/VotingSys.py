import json
from time import time
#from time import clock
from urllib.parse import urlparse
from uuid import uuid4

import subprocess
import requests
from flask import Flask, jsonify, request


class VotingSys:
    def __init__(self):
        self.voteChain = []
        self.startMiningTimer()

    
    def createVote(self, emailList):
        #Set the basic information of a new chain (port)
        fuck = 0

        #launch the blockchain as a subprocess
        
        #add the chain to self.votChain

        #send everyone a email containing the PrivateKey, ID, IP & Port


    def startMiningTimer(self):
        #Create a timer, every 10 seconds, traverse through the voteChain
        
        for k in self.voteChain:
            fuck = 0
            #send a /mine
    
    def 
    
    
        



if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
