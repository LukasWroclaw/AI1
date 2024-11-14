#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:06:14 2024

@author: ola
"""

from mainLabelClass import MainLabelClass
from fileReader import FileReader
import headerCommon as hc

testIt = 1



class MainClass:
    
    def __init__(self, filesWithText):
        
        self.filesWithText = filesWithText
        self.collectedTexts = {}       
        self.FileReader = FileReader()
        
    def collectTextFromFiles(self):
        
        for file in self.filesWithText:
            result = self.FileReader.readFile(file)
            self.collectedTexts[file] = result
        
        
    def labelCollectedFilesForKeyWord(self, keyWords, expectedSentences = None):
        self.keyWords = keyWords
        self.labelsCollectedForKeyWord = {}
        
        for keyWord in self.keyWords:
            
            self.labelsCollectedForKeyWord[keyWord] = {}
            
            for key, value in self.collectedTexts.items():
                labelClass = MainLabelClass(value)

                result = labelClass.labelSpecificKeyWord(keyWord)

                self.labelsCollectedForKeyWord[keyWord][key] = result
                
    def provideResultForSpecificKeyWordAndText(self, keyWord, textName):
        return self.labelsCollectedForKeyWord[keyWord][textName]

                 


class TestMainClass(hc.unittest.TestCase):

    def test_textCollection(self):
        
        mainClass = MainClass(["text1.odt", "text2.pdf"])
        mainClass.collectTextFromFiles()
        
        self.assertEqual(len(mainClass.collectedTexts), 2)
        
    def test_labelZiomWord(self):
        
        mainClass = MainClass(["text1.odt", "text2.pdf"])
        mainClass.collectTextFromFiles()
        
        mainClass.labelCollectedFilesForKeyWord(["Ziom"])
        
        resultOdt = mainClass.provideResultForSpecificKeyWordAndText("Ziom", "text1.odt")

        self.assertGreaterEqual(resultOdt.similarityScoreAgreggated, 0.5)
        
        resultPdf = mainClass.provideResultForSpecificKeyWordAndText("Ziom", "text2.pdf")

        self.assertLessEqual(resultPdf.similarityScoreAgreggated, -0.5)
     





if testIt:
    hc.unittest.main(argv=[''], verbosity=2, exit=False)