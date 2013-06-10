#!/usr/bin/env python
#
# Created by Aaron Beckett June 6, 2013
# Editted by:
#   Aaron Beckett
#
#
'''Program for getting system information.

Included information:
    operating system
    git hash of project (if applicable)
    python version
    installed python modules
'''

import os, sys
import subprocess

class SystemInspector:
    
    def __init__(self,extra_attributes=[]):
        # Set-up dictionary of attributes
        self.attr_names = []
        self.attributes = {}
        # Add standard attributes
        self.add_attribute('PLATFORM', sys.platform)
        self.add_attribute('PYTHON_VERSION', sys.version)
        self.add_attribute('INSTALLED_PYTHON_MODULES', sys.modules.keys())
        self.add_attribute('CLI_ARGS', ' '.join(sys.argv))
        
        # Version controll IDs
        if os.path.isdir('.git'):
            git_hash = subprocess.check_output(['git', 'log', '--pretty=format:"%H"', '-n', '1'])
            self.add_attribute('GIT_HASH', git_hash.strip('"'))
        if os.path.isdir('.svn'):
            self.add_attribute('SUBVERSION', True)
        if os.path.isdir('.hg'):
            self.add_attribute('MERCURIAL', True)
            
        # Add user provided attributes
        for attr in extra_attributes:
            self.add_attribute(attr[0],attr[1])
        
    def add_attribute(self,key,value):
        self.attr_names.append(key)
        self.attributes[key] = value
        
    def append_attributes(self,extra_attributes):
        for attr in extra_attributes:
            self.add_attribute(attr[0],attr[1])
        
    def get_attribute(self,key):
        return self.attributes[key]
            
    def write_to_file(self,filename='system_info.txt'):
        fout = open(filename, 'w')
        for attr in self.attr_names:
            st = attr + ': ' + str(self.attributes[attr]) + '\n'
            fout.write(st)
        fout.close()
        
    
    
    
    
