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

    #Triggered by the message from sponsor
    def createVote(self, emailList):
        #Set the basic information of a new chain (port)
        fuck = 0

        #launch a new blockchain as a subprocess
        
        #add the chain to self.votChain

        #add a new timer to stop the vote
        self.votingTimeCountDown()

        #send everyone a email containing the PrivateKey, ID, IP & Port
        self.sendAttenderEmail()

    def sendAttenderEmail(self, emailList):
        #send everyone a email containing the PrivateKey, ID, IP & Port


    def startMiningTimer(self):
        #Create a timer, every 10 seconds, traverse through the voteChain
        
        for k in self.voteChain:
            #if k is not finished yet 
                #send a /mine
    
    def votingTimeCountDown(self, endDate, voteInfo):
        #when time end, send specified Post to BlockChain
        # sth. like POST localhost:5000/timeEnd

    #followed func will be triggered by a message from BlockChain
    def finishVote(self, voteInfo):
        #add a tag to the chain to stop mining that chain

        #count the vote
        self.countVote()
        #set a timer to stop the blockChain after several days
        self.createFinishedVoteTimer()

    def countVote(self, voteInfo):
        #countTheVote and PrintOut(and other things)

    def createFinishedVoteTimer(self, voteInfo):
        #download all the info of that chain
        #then, delete the vote in self.voteChain
    
    
        



if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
