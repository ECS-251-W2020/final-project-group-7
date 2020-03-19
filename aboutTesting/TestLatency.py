
import json
from time import time
from time import sleep
import requests
from uuid import uuid4
from flask import Flask, jsonify, request, render_template, url_for

def testAttend(key,selection,port):
    #print("key,selection,port :  ",key," ",selection," ",port)

    newVote = {
        "sender": key,
        "recipient": selection,
        "amount": 1
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    t1 = time()

    r = requests.post("http://localhost:"+ port +"/transactions/new", json=newVote, headers = headers)
    #print(r)

    t2 = time()

    return t2-t1

def testCheck(port):
    t1 = time()

    r = requests.get("http://localhost:"+ port +"/chainDetail")
    #print(r)

    t2 = time()

    return t2-t1

def testHello(port):
    t1 = time()

    r = requests.get("http://localhost:"+ port +"/hello")
    #print(r)

    t2 = time()

    return t2-t1

def testMine(port):
    t1 = time()

    r = requests.get("http://localhost:"+ port +"/mine")
    #print(r)

    t2 = time()

    return t2-t1



t00 = 0
i = 0

while i<100:
    i+=1
    key = str(uuid4()).replace('-', '')[-16:]
    selection = "testSelection"
    port = "5001"
    t00 += testAttend(key,selection,port)
    print(i,end=" ")

print("==========================")
print("100 times of fake transfer: ",t00)
print("==========================")

# t00 = 0
# i = 0


# while i<100:
#     i+=1
#     port = "5001"
#     t00 += testCheck(port)
#     print(i,end=" ")

# print("==========================")
# print("100 times of check vote: ",t00)
# print("==========================")

# t00 = 0
# i = 0

# while i<100:
#     i+=1
#     port = "5001"
#     t00 += testHello(port)
#     print(i,end=" ")

# print("==========================")
# print("100 times of access hello: ",t00)
# print("==========================")

