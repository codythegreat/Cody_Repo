#! python3
# INCOMPLETE auto replies to craigslist job ads by sending email with resume.

import pyautogui
import time
import pyperclip
import win32clipboard
import re

# set a pause after each action
pyautogui.PAUSE = 2.5
# stop script by moving mouse to the top left
pyautogui.FAILSAFE = True

# email body. ad title will be joined between these two texts
emailText1 = `Hello,\n\nMy name is REDACTED. I'm an accountant, programmer, and graduate with a Bachelors of Business Administration in Finance. I'm replying to the Craigslist ad "`
emailText2 = `".\n\nI've attached a copy of my resume. Please feel free to contact me via email or phone.\n\nThank you,\n\n-REDACTED`

# regular expression for catching scam ads
regexScam = r'(gifts|personal funds|)'
# regular expression for finding email in ads
regexEmail = r'[\w\.-]+@[\w\.-]+'
matchedEmail = ""

adTitle = ""
adPrevTitle = ""
adBody = ""

def saveAdTitle():
	# move mouse to refresh button
	pyautogui.moveTo(x, y, duration=num_seconds)
	# click the button
	pyautogui.click()
	# move mouse to front of first post
	pyautogui.moveTo(x, y, duration=num_seconds)
	# drag across post text
	pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)
	# copy the post text
	pyautogui.hotkey('ctrl', 'c')
	# read the text
	win32clipboard.OpenClipboard()
	adTitle = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()

def saveAdBody():
	# click on ad
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()
	# check ad for scam words
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)
	pyautogui.hotkey('ctrl', 'c')
	# read the text
	win32clipboard.OpenClipboard()
	adBody = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()

def checkAdBodyScam(text):
	#checks ad text agains regular expression
	if re.match(regexScam, text, re.I):
		return True
	else:
		return False

def checkAdBodyEmail(text):
	#checks ad text agains regular expression
	email = re.search(regexEmail, text, re.I)
	if email.group(0):
		matchedEmail = email.group(0)
		return True
	else:
		return False

def checkAdReplyButton():
	# verify button by color of pixel
	if !pyautogui.pixelMatchesColor(x, y, (r, g, b), tolerance=x):
		# open reply menu
		pyautogui.moveTo(x, y, duration=num_seconds)
		pyautogui.click()
		# click gmail option
		pyautogui.moveTo(x, y, duration=num_seconds)
		pyautogui.click()
		# wait for gmail app to open
		time.sleep(5)
		return True
	else:
		return False

def respondAdTextEmail():
	# click address bar
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()
	# type gmail and hit enter
	pyautogui.typewrite('gmail', interval=secs_between_keys)
	# click new email
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()
	# click "To" field
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()
	# job email address
	pyautogui.typewrite(matchedEmail, interval=secs_between_keys)
	# Subject
	pyautogui.typewrite(adTitle, interval=secs_between_keys)
	# Body
	emailBody = emailText1 + adTitle + emailText2
	pyautogui.typewrite(emailBody, interval=secs_between_keys)
	# click send
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()

def respondAdReplyButton():
	# click inside email body
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()
	# Body
	emailBody = emailText1 + adTitle + emailText2
	pyautogui.typewrite(emailBody, interval=secs_between_keys)
	# click send
	pyautogui.moveTo(x, y, duration=num_seconds)
	pyautogui.click()

def main():
	while True:
		saveAdTitle()
		if adTitle != adPrevTitle:
			saveAdBody()
			if checkAdBodyScam(bodyText):
				if checkAdBodyEmail(bodyText):
					respondAdTextEmail()
				else if checkAdReplyButton():
					respondAdReplyButton()
		#sleep for 5 minutes after each iteration
		time.sleep(300)
	
while __name__ == '__main__':
	main()
