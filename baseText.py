#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""

import headerCommon as hc
import headerAI as hai



testIt = 1


class BaseText:

  def __init__(self, rawText = ""):
    self.document = hai.nlp(rawText)
    self.splitDocumentToSentences()
    self.sentences = []

  def splitDocumentToSentences(self):
    rawSentences = [str(i) for i in hai.nlp(self.document).sents]
    splitCharacters = [".", "\t"]
    sentencesBuffer = []
    notSplittedSentenceFlag = 0
    
    for element in rawSentences:
             
        for specChar in splitCharacters:
            if specChar in element[:-1]:
            
                sentencesBuffer.extend(element.split(specChar))
                notSplittedSentenceFlag = 1
                
        if not notSplittedSentenceFlag:
            sentencesBuffer.append(element)
            
        notSplittedSentenceFlag = 0

    
    self.sentences = sentencesBuffer
    


    return self.sentences

  def findSentencesWithSpecificKeyWord(self, keyWord):

    lowerKeyWord = keyWord.lower()

    listOfResults = []

    for sentence in self.sentences:
      if keyWord in sentence:
        listOfResults.append(sentence)
      elif lowerKeyWord in sentence:
        listOfResults.append(sentence)

    return listOfResults





class TestBaseText(hc.unittest.TestCase):

    def test_splitDocumentToSentences(self):
        base = BaseText("Parking is free for the customers. Toilet is free for the customers. No room service. Internet connection is not supported. Toilet is on the ground floor. Parking ticket is obligatory.")
        sentences = base.splitDocumentToSentences()
        self.assertEqual(len(sentences), 6)

    def test_findSentencesWithSpecificKeyWord(self):
        base = BaseText("Parking is free for the customers. Toilet is free for the customers. No room service. Internet connection is not supported. Toilet is on the ground floor. Parking ticket is obligatory.")
        base.splitDocumentToSentences()
        result = base.findSentencesWithSpecificKeyWord("Toilet")
        self.assertEqual(len(result), 2)


if testIt:
    hc.unittest.main(argv=[''], verbosity=2, exit=False)