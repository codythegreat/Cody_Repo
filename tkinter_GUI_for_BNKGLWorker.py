#! usr/bin/python3
# WORK IN PROGRESS. TO BE ADDED TO NEXT RELEASE OF BNKGLWorker.
import tkinter as tk
import Configuration
import BNKGLWorker

root = tk.Tk()
root.title('BNKGLWorker')
root.geometry('550x300')

title = tk.Label(text='Compare your bank statement\nand GL balances\n\n')
title.grid(column=1, row=0)
runButtonLabel = tk.Label(text='Select "Execute"\nto run the program.\n')
runButtonLabel.grid(column=0, row=1)
#entryFieldPerfectMatchLabel = tk.Label(text='Text to be appended for matches:')
#entryFieldPerfectMatchLabel.grid(column=0, row=2)
#entryFieldPossibleMatchLabel = tk.Label(text='\nText to be appended for possible matches:')
#entryFieldPossibleMatchLabel.grid(column=0, row=4)
configButtonLabel = tk.Label(text='Select "Configuration"\nto edit program parameters.\n')
configButtonLabel.grid(column=2, row=1)

runButton = tk.Button(text='Execute', command= lambda: BNKGLWorker.MainScript())
runButton.grid(column=0, row=2)
configButton = tk.Button(root, text='Configuration', command= lambda: ExecuteMainScript())
configButton.grid(column=2, row=2)

# for some reason this does not change the button text... need to fix
def ExecuteMainScript():
	runButton.config(text='Running')
	Configuration.ConfigEditMenu()
	runButton.config(state='normal')
	runButton.config(text='Complete!')

#TODO edit main script so that these variables are added to program
#entryFieldPerfectMatch = tk.Entry()
#entryFieldPossibleMatch = tk.Entry()
#entryFieldPerfectMatch.grid(column=0, row=3)
#entryFieldPossibleMatch.grid(column=0, row=5)		

root.mainloop()