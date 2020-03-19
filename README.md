
Doatz: A Blockchain Based E-Voting System
===
# Overview
Voting plays an important role in collective life. Traditional methods are always being questioned on privacy and credibility, while those problems can be easily solved by blockchain due to its data structure. Previous blockchain based E-voting systems mainly focus on nation-wide voting program which costs a lot of computation power and requires highly secured authentication. We build a user-friendly android application supporting universal voting scenes that are difficult to tamper and proved to be anonymous. We use mobile phone's physical information and personal ID to create unique private key to create anti-counterfeiting signature. Instead of fingerprint or other physiological characteristics, mobile phones are secure enough for daily authentication and easy to access.

# Useful link 
Trello:
https://trello.com/b/5HGOJN57/ecs251osgroup7

Summary of Progress:
https://docs.google.com/document/d/1M-j_rnqOqQrnESMdYQdU7wHGRbH4rqavMOtFe5a2pTs/edit?ts=5e4ca193

Final report slides:
https://docs.google.com/presentation/d/172o8PKVEyB7sq-lRu2rkdaajM3fFpuijsHKbSeBTBu0/edit?usp=sharing

# Doatz


## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Download the code 
```
$ git clone https://github.com/ECS-251-W2020/final-project-group-7.git
$ cd ./final-project-group-7/Doatz-master-1
```
3. Install [pipenv](https://github.com/kennethreitz/pipenv). 
```
$ pip install pipenv 
```
4. Install requirements  
```
$ pipenv install Flask==0.12.2 requests==2.18.4

``` 
** BE SURE TO re-install the enviroment every time when change folder! (because of pipenv)
5. Run the server:
    * `$ pipenv run python VotingSys.py` 
    * `$ pipenv run python VotingSys.py -p 5001`
    * `$ pipenv run python VotingSys.py --port 5002`
6. Open your browser and go to http://localhost:5000/ to create a vote
7. Fill in vote information 
8. Attend a vote and check the result
    

## Source code structure
```
Doatz-master-1
├── templates                                 # Code for frontend
├── VotingSys.py                              # Code for the voting system
│   ├── __init__()
│   ├── VotingSys                             # Voting system class
│   │   ├── createVoteChain()                 # Create a new vote
│   │   │   ├── initNewBlockChain()
│   │   │   └── calculatePortFromInfo()
│   │   ├── startMiningTimer()                # Set timer and automine the block periodically
│   │   │   └── autoMining()     
│   │   ├── votingTimeCountDown()             # Stop a vote with a deadline
│   │   │   └── SendRequest()
│   │   └── createFinishedVoteTime()          # Delete a vote chain and save its data
│   │       └── DeleteChain()
│   ├── create_vote()                         # Process frontend signal for vote creating 
│   └── attend_vote()                         # Attend a vote 
└── blockchain.py                             # Code for blockchain
    ├── Blockchain                            # Blockchain class
    │   ├──  __init__()  
    │   ├── register_node                     # Add a new node to list of nodes
    │   ├── new_block()                       # Create a new block
    │   ├── new_transaction()                 # Create a new transaction
    │   ├── resolve_conflict()                # Consensus algorithm
    │   ├── valid_chain()                     # Check if a block is valid
    │   ├── setVoteInitInfo()                 # Initialize a vote chain
    │   │   └── sendAttenderEmail()           # Send key and port to voters by email
    │   ├── countVote()                       # Tally
    │   └── printVote()                       # Print vote result
    ├── hash()                                # Creates a SHA-256 hash of a Block
    ├── proof_of_work()                       # Proof of Work Algorithm
    ├── mine()                                # Mine and add a block to chain
    ├── votingDetail()                        # Check vote chain detail
    └── DeleteChain()                         # Delete a chain and save its data
```

## Contribution
```
Juanyi Xu: Main structure design; message passing; secure design; experiment testing
Muting Wu: Email function; ballot counting; simultaneity bug fix
Yalin Zhang: Front-end development
Sicheng Mu: Timer; bug fix; README
```
