#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:10:09 2024

@author: ola
"""

import spacy
import unittest
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import spacy.cli
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

from sentence_transformers import SentenceTransformer, util


from spacy.matcher import Matcher

try:
   nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
   nltk.download('vader_lexicon')

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2') 