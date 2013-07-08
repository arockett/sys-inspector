#
#  Created by Aaron Beckett 06/19/2013
#
#
'''This Detective will be tailored to inspect and gather system information
from linux machines.'''
# Use /proc directory to gather information

from detective import Detective

class LinuxDetective(Detective):

    def __init__(self,verbose=False):
        self.verbose = verbose
