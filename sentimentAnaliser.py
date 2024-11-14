#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""

import headerCommon as hc
import headerAI as hai




testIt = 1


class SentimentAnaliser:

  def __init__(self):
    self.sia = hai.SentimentIntensityAnalyzer()

  def provideSentimentForSentence(self, sentence):
    return self.sia.polarity_scores(sentence)



class TestSentimentAnaliser(hc.unittest.TestCase):

    def test_sentimentCheck1(self):
        sentence1 = "Internet service is supported"
        analiser = SentimentAnaliser()

        result = analiser.provideSentimentForSentence(sentence1)

        self.assertGreater(result["pos"], 0.4)
        self.assertLess(result["neg"], 0.4)

    def test_sentimentCheck2(self):
        sentence1 = "Internet service is not supported"
        analiser = SentimentAnaliser()

        result = analiser.provideSentimentForSentence(sentence1)

        self.assertLess(result["pos"], 0.3)
        self.assertGreater(result["neg"], 0.3)


if testIt:
    hc.unittest.main(argv=[''], verbosity=2, exit=False)