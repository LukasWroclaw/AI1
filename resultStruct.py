#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""






class ResultStruct:
  def __init__(self, keyWord = "", sentencesWithKeyWord = [], sentimentAgreggated = 0, similarityScoreAgreggated = 0, label = 0):
    self.keyWord = keyWord
    self.sentencesWithKeyWord = sentencesWithKeyWord
    self.sentimentAgreggated = sentimentAgreggated
    self.similarityScoreAgreggated = similarityScoreAgreggated
    self.label = label