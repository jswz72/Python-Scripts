#! /usr/bin/python3
#mcb.pyw - Multiclipboard: saves/loads pieces of text to clipboard
#pwy extension means won't open terminal window when run

#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#       py.exe mcb.pwy list - Loads all keywords to clipboard

import shelve, pyperclip, sys
#sys reads commands from cmd line
#shelve used to save clipboard text
#pyperclip used to access clipboard text

mcbShelf = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
