#! python3
#Rename_Dates.py - Renames filenames form US --> European Dates 
import shutil,os,re 

dates = re.compile(r"""^(.*?)     #text before date
((0|1)?\d)-                       #one or 2 digits (month)
((0|1|2|3)?\d)-                   #one or 2 digits (day)
((19|20)                          #4 digits (year)
(.*?)$                            #text after date
""",re.VERBOSE)

for USfile in os.listdir('.'):
  mo = dates.search(USfile)
  
  #Skip files without date 
  if mo == None:
    continue;
    
  #Get the different parts of the filename 
  before = mo.group(1)
  month = mo.group(2)
  day = mo.group(4)
  year = mo.group(6)
  after = mo.group(8)
  
  #Form Euro date
  
  EUfile = before + day + '-' + month + '-' + year + after
  
  #Get full, absolute file paths
  
  abs_working_dir = os.path.abspath('.')
  USfile = os.path.join(abs_working_dir,USfile)
  EUfile = os.path.join(abs_working_dir, EUfile)
  
  #Rename the files
  print('Renaming "%s" to "%s"...' % (USfile, EUfile))
  #shutil.move(USfilename,EUfilename)   #test then uncomment
  
  
