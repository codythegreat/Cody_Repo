#! usr/bin/python3
# blackboardInformationGragger.py - a simple file to read information from 
# blackboard and write it to a txt file for offline use.

import requests
from bs4 import BeautifulSoup as bsoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import datetime

browser = webdriver.Firefox()

wait = WebDriverWait(browser, 10)


def blackboardLogin():
	browser.get('REMOVED')
	if browser.find_element_by_id('agree_button'):
		browser.find_element_by_id('agree_button').click() 		# Somtimes an "I agree" button will appear
	browser.find_element_by_id('user_id').send_keys('REMOVED')
	browser.find_element_by_id('password').send_keys('REMOVED', Keys.ENTER)
	

def blackboardCalendarScreenGrab():
	wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Calendar")))
	browser.find_element_by_link_text('Calendar').click()
	time.sleep(5)
	calendarScreenShot = browser.save_screenshot('CalendarImage' + str(datetime.datetime.now()) + '.png')

def blackboardGradesScreenGrab():
	browser.find_element_by_id('REMOVED (UNI NAME)').click()
	wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My Grades")))
	browser.find_element_by_link_text('My Grades').click()
	time.sleep(5)
	gradesScreenShot = browser.save_screenshot('GradesImage' + str(datetime.datetime.now()) + '.png')



blackboardLogin()
blackboardCalendarScreenGrab()
blackboardGradesScreenGrab()
browser.close()