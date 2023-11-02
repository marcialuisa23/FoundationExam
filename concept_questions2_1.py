# question 2.1
import re


def is_isogram(word):

    # set has no repeated characters, if length is different it is an isogram
    return len(word) > 0 and len(word) == len(set(word.lower()))

