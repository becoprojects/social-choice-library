# social-choice-library
A proof-of-concept for a python library for ordinal social welfare functions.

A Voting System can be created by initializing a VotingSystem object with a reference to a function as an input. This function must take in a Profile object, which represents a list of preferences for a series of voters, and a list of alternative in string format.

The functions in the condition_check file allows a voting system to be tested against different condition, such as Pareto Efficiency or Independance of Irrelevant Alternatives. Each of these test functions take in a voting system, a number of voters, and a set of alternatives, then generate all possible profiles with those alternatives and voters, and verify that each of the profiles conforms with the given condition.

This is not meant to prove definitivly that a given voting method always adhears to a certain condition, since it can only check the system for a fixed number of voters and alternatives, but can be used as a quick check to see if a given welfare function adhears to a condition under certain test cases, as a way to see if the system should be looked into further. As of now, any input to a check over 10 people and 3 alternatives becomes very computationally complex to check, and will take a long time as a result.