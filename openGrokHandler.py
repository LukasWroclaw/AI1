#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:10:56 2024

@author: ola
"""




import header as h
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

testIt = 1



class WebSearchClass:
    
    def __init__(self, address = "https://python.org"):
        
        options = Options()
        
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        try:
            self.driver.get(address)
        except:
            print("Connect to address fail!")
            self.driver.close()
            
    def __del__(self):
        self.driver.close()
        
    def findElementById(self, elementID = "id-search-field"):
        
        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, elementID)))
        except:
            print("findElementById fail!")
            self.driver.close()
  
            
    def findElementByName(self, elementName = "list-recent-events"):
        
        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, elementName)))
        except:
            print("findElementByName fail!")
            self.driver.close()  
            
    def findElementsByTagName(self, parentElement, tagName = "li"):
        try:
            return parentElement.find_elements(By.TAG_NAME, tagName)
        except:
            print("findElementsByTagName fail!")
            self.driver.close()  
            
            
    def sendInquiryToSearchBar(self, searchBarElement, statment = "inheritance"):
        
        try:
            searchBarElement.send_keys(statment)
            searchBarElement.send_keys(Keys.RETURN)


            
        
        except:
            print("sendInquiryToSearchBar fail!")
            self.driver.close()
        
        










class TestWebSearchClass(h.unittest.TestCase):

    def test_scenario1(self):
        
        webSearch = WebSearchClass()
        searchBar = webSearch.findElementById()
        webSearch.sendInquiryToSearchBar(searchBar, "inheritance")
        searchResults = webSearch.findElementByName()
        elements = webSearch.findElementsByTagName(searchResults, "li")

        h3Results = webSearch.findElementsByTagName(elements[0], "h3")
        textResult = h3Results[0].text


        expectedText = "Method Resolution Order"

        self.assertGreaterEqual(len(elements), 2)
        self.assertTrue(expectedText in textResult)






if testIt:
    h.unittest.main(argv=[''], verbosity=2, exit=False)


