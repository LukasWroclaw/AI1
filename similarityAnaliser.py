#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""

import header as h




testIt = 1


class SimilarityAnaliser:



  def checkSimilarity(self, sentence1, sentence2):
    sentence1Embedding = h.model.encode(sentence1, convert_to_tensor=True)
    sentence2Embedding = h.model.encode(sentence2, convert_to_tensor=True)
    result = h.util.pytorch_cos_sim(sentence1Embedding, sentence2Embedding)

    return result


class TestSimilarityAnaliser(h.unittest.TestCase):

    def test_similarityCheck1(self):

        sentence1 = "Internet service is provided."
        sentence2 = "Internet service is supported."
        analiser = SimilarityAnaliser()

        result = analiser.checkSimilarity(sentence1, sentence2)

        self.assertGreater(result, 0.8)


    def test_similarityCheck2(self):

        sentence1 = "Internet service is provided."
        sentence2 = "Internet service is not supported."
        analiser = SimilarityAnaliser()

        result = analiser.checkSimilarity(sentence1, sentence2)

        self.assertLess(result, 0.7)


if testIt:
    h.unittest.main(argv=[''], verbosity=2, exit=False)