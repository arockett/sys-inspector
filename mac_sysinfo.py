#
#  Created by Aaron Beckett 06/19/2013
#
#
'''This Detective will be tailored to inspect and gather system information
from machines that run MAC OSx.'''

from detective import Detective

class MacDetective(Detective):

    def __init__(self,verbose=False):
        self.verbose = verbose

