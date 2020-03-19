
Doatz: A Blockchain Based E-Voting System
===

# Overview
Voting plays an important role in collective life. Traditional methods are always being questioned on privacy and credibility, while those problems can be easily solved by blockchain due to its data structure. Previous blockchain based E-voting systems mainly focus on nation-wide voting program which costs a lot of computation power and requires highly secured authentication. We build a user-friendly android application supporting universal voting scenes that are difficult to tamper and proved to be anonymous. We use mobile phone's physical information and personal ID to create unique private key to create anti-counterfeiting signature. Instead of fingerprint or other physiological characteristics, mobile phones are secure enough for daily authentication and easy to access.

Trello:
https://trello.com/b/5HGOJN57/ecs251osgroup7

Summary of Progress:
https://docs.google.com/document/d/1M-j_rnqOqQrnESMdYQdU7wHGRbH4rqavMOtFe5a2pTs/edit?ts=5e4ca193

# Doatz


## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```
3. Install requirements  
```
$ pipenv install Flask==0.12.2 requests==2.18.4
``` 

4. Run the server:
    * `$ pipenv run python VotingSys.py` 
    * `$ pipenv run python VotingSys.py -p 5001`
    * `$ pipenv run python VotingSys.py --port 5002`
    
5. BE SURE TO re-install the enviroment every time when change folder! (because of pipenv)
    
## Code Structure

Basically, the Doatz-Master-1 folder is the actual main folder, look-in for the whole project.


[templates] include all the http file, and [static] include all the css, fonts, and js code.


[VotingSys.py] is what you run when launch the project.

   ├─ createVoteChain (triggered by web request)

   │        ├─ votingStartTimer ── initial vote info (send message to chain server)

   │        └─ votingTimeCountDown (control finish time)

   └─ autoMining (keep mining all the chain in list)

[blockchain.py] is the chain that will be create when requested by the VotingSys

   ├─ blockchain Control (basic function of chain)

   │        ├─ transaction accept

   │        ├─ mine

   │        └─ etc.

   ├─ initVoteMessage (add vote information to the chain)

   ├─ sendAttenderEmail (triggered when time start)

   │        └─ createCryptoKey (the way to create key, need modify for real life use)

   └─ countVote (triggered by vote result request & time end timer)

