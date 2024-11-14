#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:02:18 2024

@author: ola
"""

import headerCommon as hc
from odf import text, teletype
from odf.opendocument import load as odtLoad
from pypdf import PdfReader

testIt = 1


class FileReader:
    
    def readFile(self, fileName):
        
        extension = fileName.split(".")[1]
        
        if extension == "odt":
            return self.loadOdtFile(fileName)
        elif extension == "pdf":
            return self.loadPdfFile(fileName)
        else:
            return "NA"
            

    def loadOdtFile(self, fileName):
        textdoc = odtLoad(fileName)
        allparas = textdoc.getElementsByType(text.P)
        result = ""
        
        for element in allparas:
            result += teletype.extractText(element)
            
            
        return result


    def loadPdfFile(self, fileName):
        reader = PdfReader(fileName)
        
        result = ""
        
        for page in reader.pages:
            result += page.extract_text()
      
        return result




class TestFileReaderClass(hc.unittest.TestCase):

    def test_odtRead(self):
        
        reader = FileReader()
        result = reader.readFile("text1.odt")
        expectedText = "wiersz 1 kol 1"
        self.assertTrue(expectedText in result)
        
    def test_pdfRead(self):
        
        reader = FileReader()
        result = reader.readFile("text2.pdf")
        expectedText = "Ala ma kota $ 1"
        self.assertTrue(expectedText in result)


    def test_wrongExtRead(self):
        
        reader = FileReader()
        result = reader.readFile("text2.xvs")
        expectedText = "NA"
        self.assertTrue(expectedText in result)






if testIt:
    hc.unittest.main(argv=[''], verbosity=2, exit=False)