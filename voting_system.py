class VotingSystem:

    def __init__(self, voting_function):
        self.voting_function = voting_function

    def run(self, profile, alternatives):
        return self.voting_function(profile, alternatives)