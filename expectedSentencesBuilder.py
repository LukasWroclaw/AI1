#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""

import header as h




testIt = 1


class ExpectedSentencesBuilder:

  def __init__(self, dictOfSentencesToComplete = {"@#@ is provided" : 1, "@#@ is not provided" : -1, "There is no @#@ provided": -1}):
    self.dictOfSentencesToComplete = dictOfSentencesToComplete

  def build(self, keyWord):
    dicttWithKeyWord = {}

    for key, value in self.dictOfSentencesToComplete.items():
      key = key.replace("@#@", keyWord)
      dicttWithKeyWord[key] = value

    return dicttWithKeyWord

class TestExpectedSentencesBuilder(h.unittest.TestCase):

    def test_creationOfExpectedSentances(self):
        expectedList =  {"Internet is provided": 1, "Internet is not provided": -1, "There is no Internet provided": -1}
        builder = ExpectedSentencesBuilder()
        result = builder.build("Internet")
        self.assertEqual(result, expectedList)



if testIt:
    h.unittest.main(argv=[''], verbosity=2, exit=False)