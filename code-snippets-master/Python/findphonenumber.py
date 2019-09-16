import re
errors = []
linenum = 0
pattern = re.compile(r"(\+\d{1,2})?[\s.-]?\d{3}[\s.-]?\d{4}") # This finds telephone numbers in multiple formats: see top level of folder.
with open ('Phonenums.txt', 'rt') as myfile: # Replace Phonenums.txt with your file.
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:  # If pattern search finds a match,
            errors.append((linenum, line.rstrip('\n')))
for err in errors:
    print("Line ", str(err[0]), ": " + err[1]) # Sample out put looks like, "Line  2 : I can be reached at (331) 563-3559"
