#!/usr/bin/python3
def multiple_returns(sentence):
    sentencelength = len(sentence)
    if (sentencelength != 0):
        return (sentencelength, sentence[0])
    return (0, None)
