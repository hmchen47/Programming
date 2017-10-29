Assignment - Counting Organization
==================================

To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:

(Must have a .sqlite suffix)

Hint: The top organizational count is 536.

You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

Counting Organizations
----------------------
This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

    CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py. The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

