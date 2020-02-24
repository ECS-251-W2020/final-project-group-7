full_chain = {
  "chain": [
    {
      "index": 1,
      "previous_hash": "1",
      "proof": 100,
      "timestamp": 1582507404.8151505,
      "transactions": []
    },
    {
      "index": 2,
      "previous_hash": "223c072b9b90a3c192926fc2e8238495b4b2bb90a6596f23a2711b448f8ec859",
      "proof": 91679,
      "timestamp": 1582507742.5332482,
      "transactions": [
        {
          "amount": 1,
          "recipient": "dd02de8f183b4dd9998c6a5796206b89",
          "sender": "0"
        }
      ]
    },
    {
      "index": 3,
      "previous_hash": "aac47c054b62731de554f17d15ecfd7eecf7420e2aaa3aa4162effc4a895d850",
      "proof": 59084,
      "timestamp": 1582507818.062034,
      "transactions": [
        {
          "amount": 1,
          "recipient": "dd02de8f183b4dd9998c6a5796206b89",
          "sender": "0"
        }
      ]
    },
    {
      "index": 4,
      "previous_hash": "16ef6e2e2a204a3a1c7b5fcbe576b05d3283fa5e573b53862454ff28bdd18825",
      "proof": 50147,
      "timestamp": 1582507821.2911038,
      "transactions": [
        {
          "amount": 1,
          "recipient": "dd02de8f183b4dd9998c6a5796206b89",
          "sender": "0"
        }
      ]
    },
    {
      "index": 5,
      "previous_hash": "40e79be0e24f18eaa9ffed432496f5b554b100ca7434e110c14266455d25e7c1",
      "proof": 325369,
      "timestamp": 1582507824.835059,
      "transactions": [
        {
          "amount": 1,
          "recipient": "dd02de8f183b4dd9998c6a5796206b89",
          "sender": "0"
        }
      ]
    },
    {
      "index": 6,
      "previous_hash": "2c0021faa3107b71c4caaaac6dacfbdcc393c9a9e63ecbb0aeb3ebfe263755b0",
      "proof": 3951,
      "timestamp": 1582507880.8175511,
      "transactions": [
        {
          "amount": 1,
          "recipient": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea",
          "sender": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea"
        },
        {
          "amount": 1,
          "recipient": "dd02de8f183b4dd9998c6a5796206b89",
          "sender": "0"
        }
      ]
    },
    {
      "index": 7,
      "previous_hash": "de5caf1dea32c896ecefcefe480096b804bf1caedca962e7247e14eb00615e03",
      "proof": 6324,
      "timestamp": 1582507892.0966384,
      "transactions": [
        {
          "amount": 1,
          "recipient": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea",
          "sender": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea"
        },
        {
          "amount": 1,
          "recipient": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea",
          "sender": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea"
        },
        {
          "amount": 1,
          "recipient": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea",
          "sender": "728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea"
        },
        {
          "amount": 1,
          "recipient": "dd02de8f183b4dd9998c6a5796206b89",
          "sender": "0"
        }
      ]
    }
  ],
  "length": 7
}

print(type(chain))
Candidate_list = {}
Participant_list = {}
Candidate_list['728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea'] = 0
Participant_list['728755f3bc348a5b54d68ec8f55172078f43095b7923c2f8a48f8a8f79ec2cea'] = 6

chain = full_chain['chain']
for block in chain:
    for transaction in block['transactions']:
        print(transaction['sender'])
        if transaction['sender'] not in Participant_list:
            continue
        elif transaction['recipient'] not in Candidate_list:
            continue
        elif transaction['sender'] == '0':
            continue
        elif Participant_list[transaction['sender']] == 0:
            continue
        else:
            receiver = transaction['recipient']
            sender = transaction['sender']
            Participant_list[sender] = Participant_list[sender] - 1
            Candidate_list[receiver] = Candidate_list[receiver] + 1
            
print(Participant_list)
print(Candidate_list)
