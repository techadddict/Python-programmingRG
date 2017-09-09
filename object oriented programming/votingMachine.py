##Implement a VotingMachine class that can be used for a simple election. Have methods to
##clear the machine state, to vote for a Democrat, to vote for a Republican, and to return the total
##number of votes for both parties



class VotingMachine:
    def __init__(self):
        self.republicanCount=0
        self.democratCount=0
        
                     
        
    def voteRepublican(self):
        self.republicanCount = self.republicanCount  +  1

    def voteDemocrat(self):
        self.democratCount = self.democratCount + 1

    def unDovoteRepublican(self):
        self.republicanCount = self.republicanCount  -  1

    def unDovoteDemocrat(self):
        self.democratCount = self.democratCount - 1

    def resetRepublicanVote(self):
        self.republicanCount ==0

    def resetDemocratVote(self):
        self.democratCount ==0

    def getTotalVotesForRepublicans(self):
        return self.republicanCount

    def getTotalVotesForDemocrats(self):
        return self.democratCount


myVotingMachine = VotingMachine()
myVotingMachine.resetRepublicanVote()
myVotingMachine.voteRepublican()
myVotingMachine.voteRepublican()
myVotingMachine.voteRepublican()
myVotingMachine.unDovoteRepublican()
myVotingMachine.voteRepublican()
myVotingMachine.voteRepublican()
myVotingMachine.unDovoteRepublican()
myVotingMachine.voteRepublican()
myVotingMachine.resetDemocratVote()
myVotingMachine.voteDemocrat()
myVotingMachine.voteDemocrat()
myVotingMachine.voteDemocrat()
myVotingMachine.unDovoteDemocrat()
print(myVotingMachine.getTotalVotesForDemocrats())
print(myVotingMachine.getTotalVotesForRepublicans())                                        
    
    
