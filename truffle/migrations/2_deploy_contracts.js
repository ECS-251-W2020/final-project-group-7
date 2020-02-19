const ConvertLib = artifacts.require("ConvertLib");
const MetaCoin = artifacts.require("MetaCoin");
const Ballot = artifacts.require("Ballot");

module.exports = function(deployer) {
  deployer.deploy(ConvertLib);
  deployer.link(ConvertLib, MetaCoin);
  deployer.deploy(MetaCoin);
  //deployer.deploy(Ballot).then(function() {
  //return deployer.deploy(Ballot, TutorialToken.address);
//});
  //deployer.deploy(Ballot);
  deployer.deploy(Ballot, ['0x1234']);
};
