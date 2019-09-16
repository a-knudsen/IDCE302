# Python 3 code to rename multiple files in a directory or folder as an ordered list, eg. IDCE_1, IDCE_2, etc. From https://www.geeksforgeeks.org/rename-multiple-files-using-python/

#!/usr/bin/env python

# importing os module
import os
# Function to rename multiple files
def main():
    i = 0

    for filename in os.listdir("/Users/shadrock/Desktop/Python_Rename/"):
        dst ="IDCE_" + str(i) + ".doc"
        src ='/Users/shadrock/Desktop/Python_Rename/'+ filename
        dst ='/Users/shadrock/Desktop/Python_Rename/'+ dst

        # rename() function will rename all the files
        os.rename(src, dst)
        i += 1

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
