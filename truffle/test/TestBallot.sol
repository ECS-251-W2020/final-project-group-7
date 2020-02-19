pragma solidity >=0.4.22 <0.7.0;
import "../contracts/Ballot.sol";
import "truffle/DeployedAddresses.sol";
import "truffle/Assert.sol";

contract vote{

        function beforeAll() public {
          // here should instantiate tested contract
          Assert.equal(uint(4), uint(3), "error in before all function");
        }

        function check1() public {
          // use 'Assert' to test the contract
          Assert.equal(uint(2), uint(1), "error message");
          Assert.equal(uint(2), uint(2), "error message");
        }

        function check2() public view returns (bool) {
          // use the return value (true or false) to test the contract
          return true;
        }
      }

    contract test_2 {

      function beforeAll() public {
        // here should instantiate tested contract
        Assert.equal(uint(4), uint(3), "error in before all function");
      }

      function check1() public {
        // use 'Assert' to test the contract
        Assert.equal(uint(2), uint(1), "error message");
        Assert.equal(uint(2), uint(2), "error message");
      }

      function check2() public view returns (bool) {
        // use the return value (true or false) to test the contract
        return true;
      }
    }

    contract TestBallot{

        bytes32[] proposalNames;

        Ballot ballotToTest;
        function beforeAll () public {
            //proposalNames.push(bytes32('0x1234'));
            proposalNames.push('0x1234');
            ballotToTest = new Ballot(proposalNames);
        }

        function testWinningProposal () public {
            ballotToTest.vote(0);
            Assert.equal(ballotToTest.winningProposal(), uint(0), "proposal at index 0 should be the winning proposal");
            Assert.equal(ballotToTest.winnerName(), '0x1234', "candidate1 should be the winner name");
        }

        function testWinninProposalWithReturnValue () public view returns (bool) {
            return ballotToTest.winningProposal() == 0;
        }
    }
