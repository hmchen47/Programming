
# 7.2 Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the 
# lines and compute the average of those values and produce an output as 
# shown below.
# You can download the sample data at 
# http://www.pythonlearn.com/code/mbox-short.txt when you are testing 
# below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")

num_lines = 0
sum_dspam = 0.0;

cpos = spos = epos = 0

try:
    fh = open(fname)
except ValueError:
    print "Cannot not open file: ", fname
    exit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    else: 
#       print line
        line = line.rstrip()
        try:
            cpos = line.index(':')
            substr = (line[cpos+1:]).lstrip()
#            print str
            sum_dspam = sum_dspam + float(substr)
#            print sum_dspam
            num_lines = num_lines + 1
#            print num_lines
        except ValueError:
            print "Unable to find \":\" in line", line
            continue

print "Average spam confidence:", sum_dspam/num_lines