
from __future__ import print_function
import string
import re
import unittest




def word_cloud(input):
    """map string of words into a dict of word frequencies"""

    sentence_enders = r"\.|!|\?"
    sentences = re.split(sentence_enders, input)

    freq = {}
    for sentence in sentences:
        words = re.split(r"[^a-zA-Z0-9-]+", sentence)
        for word in words:
            count = freq.get(word, 0)
            freq[word] = count + 1

    def is_cap(word):
        ch = word[0:1]
        return ch in string.uppercase

    for word, count in freq.items():
        if is_cap(word) and word.lower() in freq:
            count = freq[word]
            freq[word.lower()] += count
            del freq[word]

    return freq
