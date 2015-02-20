from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

from mutagen.mp3 import MP3
import sys, os

pathname = os.path.abspath(sys.argv[1])
audio = MP3(pathname)
title = audio["TIT2"]
comp = audio["TPE1"]


def getsheetmusic():
	print 'Opening browser...'
	browser = webdriver.Chrome() # Get local session of Chrome
	browser.get("http://www.imslp.org") # Load page
	print 'Searching IMSLP...'
	search = browser.find_element_by_name('sbox') # find search box element
	search.send_keys('%s %s' % (comp, title))
	search.send_keys(Keys.RETURN)
	time.sleep(2) # wait 2 secs
	browser.find_element_by_xpath("//*[@id='rso']//div//h3/a").click()
	time.sleep(2)
	# find numerical values of rating elements and index
	ratings = []
	for elem in browser.find_elements_by_xpath('.//span[@class = "current-rating"]'):
		ratings.append(elem.text)
	x = ratings.index(max(ratings))
	# to visualize, for my own benefit
	for i, j in enumerate(ratings):
		print i, j
	print ratings.index(max(ratings))
	time.sleep(1)
	# choose the download link that corresponds to index of highest rated link
	dl = browser.find_elements_by_xpath('.//span[@title = "Download this file"]')[x]
	dl.click()
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="bodyContent"]/center/a').click()

	print 'Sheet Music Found.'

getsheetmusic()
