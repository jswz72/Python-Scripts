#!python3
#backup_to_zip.py
#copies entire folder and its contents into a ZIP file, named incrementally

import zipfile, os

def backup_to_zip(folder):
  #Backup the entire contents of "folder" into a ZIP folder
  folder = os.path.abspath(folder)  #make sure folder is absolute
  
  #Check to see if any previous backups
  number = 1
  while True:
    zipfile_name = os.path.basename(folder) + '_' + str(number) + '.zip.'
    if not os.path.exists(zipfile_name):
      break;
    number += 1;
    
  print('Creating %s...' % (zipfile_name))
  backup_zip = zipfile.ZipFile(zipfile_name,'w')
  
  for foldername, subfolders, filenames in os.walk(folder):
    print('Adding files in %s...' % (foldername))
    #Add current folder to ZIP file 
    backup_zip.write(foldername)
    #Add all the files in this folder to ZIP file 
    for filename in filenames:
      new_base = os.path.basename(folder) + '_'
      if filename.startswith(new_base) and filename.endswith('.zip'):
        continue  #dont need to backup if already zipped
      backup_zip.write(os.path.join(foldername, filename))
  
  backup_zip.close()
  print('Done')
backup_to_zip('') #call function with intended folder
