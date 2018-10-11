#! usr/bin/python3
# WORK IN PROGRESS. TO BE ADDED TO NEXT RELEASE OF BNKGLWorker.

import tkinter as tk
#TODO rework main file to use as an import
#TODO create file for config code that can be imported

window = tk.Tk()
window.title('BNKGLWorker')
window.geometry('770x450')

title = tk.Label(text='Compare your bank statement\nand GL balances\n\n')
title.grid(column=1, row=0)
runButtonLabel = tk.Label(text='Select "Execute"\nto run the program.\n')
runButtonLabel.grid(column=0, row=1)
entryFieldPerfectMatchLabel = tk.Label(text='Text to be appended for matches:')
entryFieldPerfectMatchLabel.grid(column=0, row=2)
entryFieldPossibleMatchLabel = tk.Label(text='\nText to be appended for possible matches:')
entryFieldPossibleMatchLabel.grid(column=0, row=4)
configButtonLabel = tk.Label(text='Select "Configuration"\nto edit program parameters.\n')
configButtonLabel.grid(column=2, row=1)

#TODO link main script and config setup script into GUI
runButton = tk.Button(text='Execute',) #command=mainBNKGLWorker()) To be used later
runButton.grid(column=0, row=6)
configButton = tk.Button(text='Configuration',) #command=launchUserConfigSetup()) To be used later
configButton.grid(column=2, row=2)
#TODO edit main script so that these variables are added to program
entryFieldPerfectMatch = tk.Entry()
entryFieldPossibleMatch = tk.Entry()
entryFieldPerfectMatch.grid(column=0, row=3)
entryFieldPossibleMatch.grid(column=0, row=5)		

window.mainloop()
