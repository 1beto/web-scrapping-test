import time
import numpy as np
import csv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#to use eager strategies
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup


binary = r'/usr/bin/firefox'
#god said me that I should do this
options = Options()
options.binary_location = binary

#i don't want to wait the whole page to load
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['PAGE_LOAD_STRATEGY'] = 'eager'

browser = webdriver.Firefox(options=options,
                            desired_capabilities=capabilities)
browser.get("https://www.extra.com.br/?Filtro=D25515")

itens = browser.find_elements_by_categories('link url')

#opening a file to save the targeted informations
#only testing the name of the product
with open('info.csv', 'w') as csv_output:
	writer = csv.writer(csv_output)
	
	for item in itens:
		data = [] #all of the targeted information
		
		#PROBLEM: PAGE NOT LOADING
		#(but works on a simpler case)	
		item.click()
		
		#I can't test to know if name is redundant after myElem
		myElem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//b[@itemprop='name']")))		
		#browser.implicitly_wait(30)
		name = browser.find_element_by_xpath(
					 "//b[@itemprop='name']")
		
		print(name,myElem)
