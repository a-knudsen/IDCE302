# This code removes the beginning of a file name and can be used for all the files in a directory. 
#!/usr/bin/env python
import os # This imports the os module.
os.chdir('/Users/shadrock/Desktop/Python_Rename') # Replace with full path of chosen directory. Mac users can just drag a file into terminal to get the full path name.
for filename in os.listdir('.'):
    if filename.startswith('IDCE 302_'):
        os.rename(filename, filename[9:]) # Here, the value of 9 corresponds to the unwated file beginning of "IDCE 302_"
