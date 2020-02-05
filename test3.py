
from __future__ import print_function
import string
import re
import unittest

input = 'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

sentence_enders = r"\.|!|\?"
sentences = re.split(sentence_enders, input)

freq = {}
for sentence in sentences:
    words = re.split(r"[^a-zA-Z0-9-]+", sentence)

print(words)