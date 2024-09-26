#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""

import header as h




testIt = 1


class BaseText:

  def __init__(self, rawText = ""):
    self.document = h.nlp(rawText)
    self.splitDocumentToSentences()

  def splitDocumentToSentences(self):
    self.sentences = [i for i in h.nlp(self.document).sents]

    return self.sentences

  def findSentencesWithSpecificKeyWord(self, keyWord):

    lowerKeyWord = keyWord.lower()

    listOfResults = []

    for sentence in self.sentences:
      if keyWord in sentence.text:
        listOfResults.append(sentence)
      elif lowerKeyWord in sentence.text:
        listOfResults.append(sentence)

    return listOfResults





class TestBaseText(h.unittest.TestCase):

    def test_splitDocumentToSentences(self):
        base = BaseText("Parking is free for the customers. Toilet is free for the customers. No room service. Internet connection is not supported. Toilet is on the ground floor. Parking ticket is obligatory")
        sentences = base.splitDocumentToSentences()
        self.assertEqual(len(sentences), 6)

    def test_findSentencesWithSpecificKeyWord(self):
        base = BaseText("Parking is free for the customers. Toilet is free for the customers. No room service. Internet connection is not supported. Toilet is on the ground floor. Parking ticket is obligatory")
        base.splitDocumentToSentences()
        result = base.findSentencesWithSpecificKeyWord("Toilet")
        self.assertEqual(len(result), 2)


if testIt:
    h.unittest.main(argv=[''], verbosity=2, exit=False)