import json
import threading
from time import time
#from time import clock
from urllib.parse import urlparse
from uuid import uuid4

# create subprocess
import subprocess

# create timer
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import requests
from flask import Flask, jsonify, request



class VotingSys:
    def __init__(self):
        self.voteChain = []
        #self.startMiningTimer()        
        self.port = 5000 #use 5000 as defort port
        #self.newChainPort = self.port

    #Triggered by the message from sponsor
    def createVoteChain(self, voteIntro, candidate, emailList, startTime, endTime):

        print("===============================================")
        print(time())    
        print("============TESTING CREATE CHAIN===============") 
        print("===============================================")

        #Set the basic information of a new chain (port)
        
        newChain = {
            'index': len(self.voteChain),
            'timestamp': time(),
            'voteIntro': voteIntro,
            'candidate': candidate,
            'emailList': emailList,
            'startTime': startTime,
            'endTime': endTime,
            'port': str(self.calculatePortFromInfo( voteIntro , len(self.voteChain)+1 )),
            'password': str(uuid4()).replace('-', '')[-6:]
        }

        #print(newChain)
        

        #launch a new blockchain as a subprocess                
        loader = subprocess.Popen(["pipenv","run","python","blockchain.py","-p",newChain['port'],"-k",newChain['password']])
        # I wonder if we can do sth. with loader
       
        #add the chain to self.voteChain
        self.voteChain.append(newChain)

        #print(self.voteChain)

        #print(type(self.voteChain))

        #start initialize the vote
        #save the Vote Info to the chain (by send sth. like a transfer)
        self.initNewBlockChain(newChain['index'])
        
        #then set a timer to start the vote in time
        self.votingStartTimer(newChain['index'],startTime)

        #add a new timer to stop the vote
        self.votingTimeCountDown(newChain['index'],endTime)
    
    def calculatePortFromInfo(self, voteIntro, voteIndex):
        #set the port (should be crypto before sending email, now only for test)
        return self.port + voteIndex

    # probably this should be done by BlockChain
    def sendAttenderEmail(self, emailList):
        #send everyone a email containing the PrivateKey, ID, IP & Port
        return

    def initNewBlockChain(self, voteIndex):
        #send message to BlockChain to init the forst several block and create crypto key
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        #print(voteIndex)
        #print(self.voteChain[voteIndex])
        r = requests.post("http://localhost:5001/initVote", json=self.voteChain[voteIndex], headers = headers)

        print(r)
        return


    def autoMining(self):
        for k in self.voteChain:
            #if time()>k['startTime'] and time()<k['endTime']:    #if k is not finished yet
            if True:
                r = requests.get("http://localhost:"+k['port']+"/mine")
                #print(r.json())

    def startMiningTimer(self):
        #Create a timer, every 10 seconds, traverse through the voteChain
        scheduler = BlockingScheduler()
        scheduler.add_job(self.autoMining, 'interval', seconds=10, id='test_job1')
        scheduler.start()
        
    
    def votingStartTimer(self, voteIndex, startTime):
        # set a timer, when vote start, tell BlockChain to send email to attender

        # post : /sendStartEmail ["key":"xxx"]


        return

    def votingTimeCountDown(self, voteIndex, endTime):
        # set a timer, when time end, send specified Post to BlockChain

        # post: /voteTimeEnd ["key":"xxx"]
        # the key here should be set later in the project

        return


    #followed func will be triggered by a message from BlockChain
    def finishVote(self, voteIndex):
        #1 check the vote time is ended
        if self.voteChain[voteIndex]['endTime']<time():
            return {"warning":"VOTE have NOT finished yet!!!"}

        #2 check the chain to see if it did recieved the special message

        # I guess this can be done by countVote()
        #if self.checkMineOut(voteIndex) :
        #    return {"warning":"VOTE have NOT finished yet!!!"}

        #3 count the vote and printout result
        xxx = self.countVote(voteIndex)

        #if xxx['finish'] == 0 :
        #    return {"warning":"VOTE have NOT finished yet!!!"}
        
        #4 set a timer to stop the blockChain after several days
        self.createFinishedVoteTimer(voteIndex)

        return xxx

    def countVote(self, voteIndex):
        #countTheVote and PrintOut(and other things)


        return 

    def createFinishedVoteTimer(self, voteIndex):
        # set a timer, download all the info of that chain
        #then, shutdown that block chain, and delete the vote in self.voteChain



        return
    
    

app = Flask(__name__)
# Instantiate the VotingSystem
votingSystem = VotingSys()

@app.route('/hello', methods=['GET'])
def helloWorld():
    print("hello world")
    return jsonify({"message":"hello world"}), 201

@app.route('/createVote', methods=['POST'])
def createVote():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    required = ['voteIntro', 'candidate', 'emailList', 'startTime', 'endTime']
    # mayby deal with Possible fields like 'voteName', 'briefIntro' later...

    if not all(k in values for k in required):
        return 'Missing values', 400
    
    #Create the chain
    xxx = votingSystem.createVoteChain(values['voteIntro'], values['candidate'], values['emailList'], values['startTime'], values['endTime'])

    ###################
    ## design sth. to return 
    ###################

    return jsonify(xxx), 201

@app.route('/voteFinish', methods=['POST'])
def mineOutSpecialInfo():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    required = ['voteIndex']

    if not all(k in values for k in required):
        return 'Missing values', 400

    xxx = votingSystem.finishVote(values['voteIndex'])

    ###################
    ## design sth. to return 
    ###################

    return jsonify(xxx), 202


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    votingSystem.port = port

    t1 = threading.Thread(target=app.run, args=('0.0.0.0',port))
    t2 = threading.Thread(target=votingSystem.startMiningTimer)
    t1.start()
    t2.start()
    #app.run(host='0.0.0.0', port=port)


