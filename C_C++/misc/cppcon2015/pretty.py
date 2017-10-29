import time

class StudentPrinter(object):
    """Print a struct student"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        # check format syntax --> seems not working
        # the index must be string for dictionary, e.g. tm_mon --> 'tm_mon'
        print("month = %d" %self.val['dob']['tm_mon'])

        # find the way to print in format syntax
        return ("id = %i name=%s dob='%s'"
                % (self.val['id'], self.val['name'],
                    time.asctime(
                        (self.val['dob']['tm_year']+1900,
                         self.val['dob']['tm_mon'],
                         self.val['dob']['tm_mday'],
                         self.val['dob']['tm_hour'],
                         self.val['dob']['tm_min'],
                         self.val['dob']['tm_sec'],
                         self.val['dob']['tm_wday'],
                         self.val['dob']['tm_yday'],
                         self.val['dob']['tm_isdst']
                        )
                    )))

    def display_hint(self):
        return 'student'

import gdb.printing
pp = gdb.printing.RegexpCollectionPrettyPrinter('student')
pp.add_printer('student', '^student$', StudentPrinter)
gdb.printing.register_pretty_printer(gdb.current_objfile(), pp)
