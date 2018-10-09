#! python3
# bankstatementscript.pyw - A program that will compare values from the GL and
# bank statement for matches.

import os
import shutil
import configparser
import re
import PyPDF2
import openpyxl
from string import ascii_letters

def ConfigSetup():
	print('Initializing user config setup. When prompted to enter file locations, please use the following format:')
	print('C:\\user\\yourname\\path\\to\\your\\file')
	print('or if your file is inside the BNKGLWorker_config folder, simply input the file name.')
	user_config = configparser.ConfigParser()
	print('Setting up file inputs...')
	user_config.add_section('file_inputs')
	print('input the file location of the bankstatment excel sheet to be created:')
	user_config['file_inputs']['bankStatementExcel'] = input()
	print('input the file location of the bankstatment PDF file:')
	user_config['file_inputs']['bankStatementPDF'] = input()
	print('input the excel file containing the GL amounts:')
	user_config['file_inputs']['bankRecExcel'] = input()
	print('Setting up Excel settings...')
	user_config.add_section('excel_settings')
	print('input the sheet containing your GL amounts:')
	user_config['excel_settings']['sheetGL'] = input()
	print('input the starting cell of your GL amounts:')
	user_config['excel_settings']['startingCell'] = input()
	with open('user_config.ini', 'w') as f:
		user_config.write(f)	


def bankStmntPDFtoExcelConversion():
	cashAmountsRegex = re.compile(r"\d+?,?\d+\.\d{2}\-?")
	cashAmounts = []
	pagesinPDF = bankStatementPDFReader.numPages
	for i in range(pagesinPDF):
		pageObj = bankStatementPDFReader.getPage(i)
		textFromPage = pageObj.extractText()
		textFromPage.replace(',','')
		for i in cashAmountsRegex.findall(textFromPage):
			cashAmounts.append(i)
	for i in range(len(cashAmounts)):
		if '-' in cashAmounts[i]:
			cashAmounts[i] = '-' + cashAmounts[i][:-1]
		sheetBnkStmnt['C' + str(3 + i)] = cashAmounts[i]


def extractGLAmountsfromExcel():
	for rowOfGLAmounts in sheetGL[sheetGLStartingCell : sheetGLStartingCell[0] + str(sheetGL.max_row)]:
		for amount in rowOfGLAmounts:
			amountsOnGL.append(amount.value)



def extractBankStmntAmountsfromExcel():
	for rowOfBnkStmntAmounts in sheetBnkStmnt['C3' : 'C' + str(sheetBnkStmnt.max_row)]:
		for amount in rowOfBnkStmntAmounts:
			amountsOnBnkStmnt.append(amount.value)


def exactMatchTester():
	for i in range(len(amountsOnGL)):
		for j in range(len(amountsOnBnkStmnt)):
			try:
				if float(amountsOnGL[i]) == float(amountsOnBnkStmnt[j]):
					#sheetGL['G' + str(25 + i)] = 'Perfect Match!'
					sheetBnkStmnt['D' + str(3 + j)] = 'Perfect Match!'
					sheetGL[rLetter + str(int(sheetGLStartingCell[1:]) + i)] = 'Perfect Match!'
			except:
				continue


def alternativeMatchTester():
	for i in range(len(amountsOnGL)):
		for j in range(len(amountsOnBnkStmnt)):
			for k in range(len(amountsOnGL)):
				try:
					if float(amountsOnGL[i]) + float(amountsOnGL[k]) == float(amountsOnBnkStmnt[j]):
						#sheetGL['G' + str(25 + i)] = 'match with G' + str(25 + k)
						sheetBnkStmnt['D' + str(3 + j)] = 'Possible match with ' + str(sheetGLStartingCell[0] + str(i) + ' and ' + str(k))
						sheetGL[rLetter + str(int(sheetGLStartingCell[1:]) + i)] = 'Possible match with ' + str(sheetGLStartingCell[0]) + str(k)	
				except:
					continue 


def saveandCloseExcelBooks():
	bankStatementExcel.save(user_config['file_inputs']['bankStatementExcel'])
	bankRecExcel.save(user_config['file_inputs']['bankRecExcel'])



config_dir = os.path.expanduser("~") + "/BNKGLWorker/config"
print(config_dir)
config = config_dir + "/user_config.ini"

if not os.path.isfile(config):
    os.makedirs(config_dir, exist_ok=True)
    os.chdir(os.path.expanduser("~") + "/BNKGLWorker/config")
    ConfigSetup()

user_config = configparser.ConfigParser()
user_config.read(config)

os.chdir(os.path.expanduser("~") + "/BNKGLWorker")


while True:
	print('Welcome to BNKGLWorker!')
	print('Input A to run BNKGLWorker based on config file, or input B to launch config edit.')
	choice = input().upper()
	if choice == 'B':
		ConfigSetup()

	elif choice == 'A':

		bankStatementPDF = open(user_config['file_inputs']['bankStatementPDF'], 'rb')
		bankStatementPDFReader = PyPDF2.PdfFileReader(bankStatementPDF)

		bankRecExcel = openpyxl.load_workbook(user_config['file_inputs']['bankRecExcel'])
		bankStatementExcel = openpyxl.Workbook()

		sheetGL = bankRecExcel[user_config['excel_settings']['sheetGL']]
		sheetGLStartingCell = user_config['excel_settings']['startingCell']
		sheetBnkStmnt = bankStatementExcel['Sheet']

		amountsOnGL = []
		amountsOnBnkStmnt = []
		rLetter = ascii_letters[ascii_letters.index(sheetGLStartingCell[0]) + 1]

		#################################################################################
		
		bankStmntPDFtoExcelConversion()
		extractGLAmountsfromExcel()
		extractBankStmntAmountsfromExcel()
		alternativeMatchTester()
		exactMatchTester()
		saveandCloseExcelBooks()
		print('Done')
		break