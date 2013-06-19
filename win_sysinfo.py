#
#  Created by Aaron Beckett 06/19/2013
#
#
'''This Detective will be tailored to inspect and gather system information
from Windows 32-bit machines.'''

from detective import Detective

class WindowsDetective(Detective):

    def __init__(self,verbose=False):
        self.verbose = verbose

