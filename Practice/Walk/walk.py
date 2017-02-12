#! /usr/bin/python3
import os


print('Enter path to scan')
path = input()

while True:
    if os.path.exists(path):
        for folder_name, subfolders, filenames in os.walk(path):
            print('\nCURRENT FOLDER: ' + folder_name)
            for subfolder in subfolders:
                print('\tSUBFOLDER: ' + subfolder)
            for filename in filenames:
                print('\tFILE:' + filename)

            print('')
        print('\nENTER PATH OR TYPE "Q" TO QUIT')
        path = input()
        if path == 'Q':
            break;
    else:
        print('PATH DOESN\'T EXIST')
        print('\nENTER PATH TO SCAN OR TYPE "Q" TO QUIT')
        path = input()
        if path == 'Q':
            break;
        

