
# 7.1 Write a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# You can download the sample data at 
# http://www.pythonlearn.com/code/words.txt

# Use words.txt as the file name
fname = raw_input("Enter file name: ");

try:
	fh = open(fname);
except ValueError:
	print 'File cnanot be opened:', fname;
	exit ();

count = 0
for line in fh:
	line = line.rstrip();
	print line.upper();

	