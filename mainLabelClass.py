#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""

import header as h
from resultStruct import ResultStruct
from baseText import BaseText
from sentimentAnaliser import SentimentAnaliser
from similarityAnaliser import SimilarityAnaliser
from expectedSentencesBuilder import ExpectedSentencesBuilder

testIt = 1

class MainLabelClass:

  def __init__(self, textToAnalize = ""):

    self.baseText = BaseText(textToAnalize)
    self.sentences = self.baseText.splitDocumentToSentences()

    self.sentimentAnaliser = SentimentAnaliser()

    self.similarityAnaliser = SimilarityAnaliser()

  def agreggateSentiment(self, sentence):
        sentimentResult = self.sentimentAnaliser.provideSentimentForSentence(str(sentence))
        self.aggregatedSentiment += sentimentResult["pos"]
        self.aggregatedSentiment -= sentimentResult["neg"]


  def agreggateSimilarity(self, sentence, dictExpectedSentences, threshold = 0.75):

    for key, value in dictExpectedSentences.items():

      result = self.similarityAnaliser.checkSimilarity(str(sentence), key)

      if result >= threshold:
        self.similarityScoreAgreggated += value






  def labelSpecificKeyWords(self, keyWords = [""]):

    analizedKeyWords = []
    sentencesBuilder = ExpectedSentencesBuilder({"@#@ is provided" : 1, "@#@ is not provided" : -1, "There is no @#@ provided": -1, "@#@ is supported" : 1})

    for element in keyWords:

      self.aggregatedSentiment = 0
      self.similarityScoreAgreggated = 0

      sentencesWithKeyWord = self.baseText.findSentencesWithSpecificKeyWord(element)
      dictExpectedSentences = sentencesBuilder.build(element)

      for sentence in sentencesWithKeyWord:
        self.agreggateSentiment(sentence)
        self.agreggateSimilarity(sentence, dictExpectedSentences, 0.75)


      analizedKeyWords.append(ResultStruct(element, sentencesWithKeyWord, self.aggregatedSentiment, self.similarityScoreAgreggated, 0))
      print("%%%%", element, sentencesWithKeyWord, self.aggregatedSentiment, self.similarityScoreAgreggated)

    return analizedKeyWords


class TestLabelClass(h.unittest.TestCase):

    def test_label1(self):

        text = "Hotel book in hour to 10 pm. Check out till 10 am. Pets are allowed. Internet is provided. Additional payment for internet outsite. Toilet in every room. Internet service is supported."
        keyWords = ["Internet", "Toilet"]

        labelClass = MainLabelClass(text)

        result = labelClass.labelSpecificKeyWords(keyWords)

        self.assertEqual(len(result), 2)
        self.assertGreaterEqual(result[0].sentimentAgreggated, 0)
        self.assertEqual(result[0].label, 0)
        self.assertEqual(len(result[0].sentencesWithKeyWord), 3)


    def test_label2(self):
      text = "Nearly a week after the grand unveiling of the iPhone 16 series, Apple has finally confirmed one of the key specs for these new flagship phones: all of the models in the range are fitted with 8GB of RAM.As spotted by 9to5Mac, Apple executive Johny Srouji confirmed the 8GB amount in an interview with Geekerwan. Apple doesn't include RAM in the official spec sheets for its iPhones, for whatever reason, so some detective work is usually required to establish how much memory these handsets have inside.A few days ago, code spotted in an official Apple developer tool suggested that all the iPhone 16 models were indeed fitted with 8GB of RAM, and now we have confirmation. Last year the iPhone 15 Pro and iPhone 15 Pro Max had 8GB of RAM inside, while the iPhone 15 and iPhone 15 Plus made do with 6GB."
      keyWords = ["RAM"]

      labelClass = MainLabelClass(text)

      result = labelClass.labelSpecificKeyWords(keyWords)

      self.assertEqual(len(result), 1)
      self.assertGreaterEqual(result[0].sentimentAgreggated, 0)
      self.assertEqual(result[0].label, 0)
      self.assertEqual(len(result[0].sentencesWithKeyWord), 4)


if testIt:
    h.unittest.main(argv=[''], verbosity=2, exit=False)