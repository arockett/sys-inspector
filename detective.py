#
#  Created by Aaron Beckett 06/19/2013
#
#
'''The abstract Detective object to be inherited by all Detectives.'''


class Detective:

    def __init__(self,verbose=False):
        '''Override this method to gather all raw system info in a usable
        format that can be accessed by other functions in Detective.
        It is ok to gather too much info here because the rest of 
        Detective's methods pick out the most important pieces from the
	"master list" of information generated here.'''
	# self.verbose: is True if user wants to record ALL info gathered
	#               in __init__ and not just the key attributes.
	self.verbose = verbose
        raise NotImplementedError

    def get_processor(self):
	'''Override this method to pick out and return the processor type 
	from the "master list" of system information.'''
	raise NotImplementedError

    def get_total_mem(self):
	raise NotImplementedError

    def get_used_mem(self):
	raise NotImplementedError

    def get_free_mem(self):
	raise NotImplementedError

    def write_all(self):
	if self.verbose:
	    # Save ALL info gathered in __init__ in an appropriate format.
	    pass
	raise NotImplementedError
