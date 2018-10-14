#! usr/bin/python3
#TODO make this a stand alone file where anythin config related will occur

import configparser
import os
import tkinter as tk

config_dir = os.path.expanduser("~") + "/BNKGLWorker/config"
config = config_dir + "/user_config.ini"
if not os.path.isfile(config):
    os.makedirs(config_dir, exist_ok=True)
os.chdir(config_dir)
user_config = configparser.ConfigParser()

def ConfigEditMenu():

    configWindow = tk.Toplevel()
    configWindow.geometry('410x450')

    title = tk.Label(configWindow, text='Input config parameters below:\n\n')
    title.grid(column=0, row=0)

    labelPDFLocation = tk.Label(configWindow, text='Location of PDF file:')
    labelBankExcelLocation = tk.Label(configWindow, text='Location of Bank Excel file:')
    labelGLExcelLocation = tk.Label(configWindow, text='Location of GL Excel file:')
    labelGLSheet = tk.Label(configWindow, text='GL sheet containing amounts:')
    labelGLStartingCell = tk.Label(configWindow, text='Starting cell of amounts:')

    labelPDFLocation.grid(column=0, row=1)
    labelBankExcelLocation.grid(column=0, row=3)
    labelGLExcelLocation.grid(column=0, row=5)
    labelGLSheet.grid(column=0, row=7)
    labelGLStartingCell.grid(column=0, row=9)

    entryFieldPDFLocation = tk.Entry(configWindow, width=50)
    entryFieldBankExcelLocation = tk.Entry(configWindow, width=50)
    entryFieldGLExcelLocation = tk.Entry(configWindow, width=50)
    entryFieldGLSheet = tk.Entry(configWindow, width=10)
    entryFieldGLStartingCell = tk.Entry(configWindow, width=10)

    entryFieldPDFLocation.grid(column=0,row=2)
    entryFieldBankExcelLocation.grid(column=0,row=4)
    entryFieldGLExcelLocation.grid(column=0,row=6)
    entryFieldGLSheet.grid(column=0,row=8)
    entryFieldGLStartingCell.grid(column=0,row=10)

    buttonSubmit = tk.Button(configWindow, text='Submit', command= lambda: ConfigGenerator())
    buttonSubmit.grid(column=0, row=11)

    def ConfigGenerator():
        
        user_config.add_section('file_inputs')
        user_config['file_inputs']['bankStatementExcel'] = entryFieldBankExcelLocation.get()
        user_config['file_inputs']['bankStatementPDF'] = entryFieldPDFLocation.get()
        user_config['file_inputs']['bankRecExcel'] = entryFieldGLExcelLocation.get()

        user_config.add_section('excel_settings')
        user_config['excel_settings']['sheetGL'] = entryFieldGLSheet.get()
        user_config['excel_settings']['startingCell'] = entryFieldGLStartingCell.get()

        with open('user_config.ini', 'w') as f:
            user_config.write(f)