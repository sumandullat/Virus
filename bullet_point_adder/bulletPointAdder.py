#! python3
# bulletPointAdder.py - Adds wikipedia bullet points to the start of each line of the the text on the clipboard

import pyperclip
clipboard = pyperclip.paste()

lines = text.split('\n') #Separate lines and add stars
for i in range(len(lines)): # loop through all all indexes in the "lines" list
	lines[i] = '*' + lines[i] # add star to each string in "lines" list
#Add...
clipboard = '\n'.join(lines) # transform "lines" lsit to one single string value
clipboard = pyperclip.paste()

# tldr: use clipboard as in or output...