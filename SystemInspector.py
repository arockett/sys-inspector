#!/usr/bin/env python
#
# Created by Aaron Beckett June 6, 2013
# Editted by:
#   Aaron Beckett
#
#
'''Module for easily storing current system information during program execution.

Included information:
    operating system
    python version
    installed python modules
    command line arguments used
    git hash of project (if applicable)
'''

import os, sys
import subprocess

class SystemInspector:

    def __init__(self,extra_attributes=[]):
        # Set-up dictionary of attributes
        self.attr_names = []
        self.attributes = {}

        # Add user provided attributes first for convenient referencing
        self.append_attributes(extra_attributes)

        # Add standard attributes
        self.add_attribute('PLATFORM', sys.platform)
        self.add_attribute('PYTHON_VERSION', sys.version)
        self.add_attribute('PYTHON_DIR', sys.executable)
        self.add_attribute('PYTHON_PATH', sys.path)
        self.add_attribute('INSTALLED_PYTHON_MODULES', sys.modules.keys())
        self.add_attribute('FLOAT_INFO', sys.float_info)
        self.add_attribute('MAX_INT', sys.maxint)
        self.add_attribute('MAX_SIZE', sys.maxsize)
        self.add_attribute('FILE_SYSTEM_ENCODING', sys.getfilesystemencoding())
        self.add_attribute('CLI_ARGS', ' '.join(sys.argv))

        # Version controll IDs
        if os.path.isdir('.git'):
            git_hash = subprocess.check_output(['git', 'log', '--pretty=format:"%H"', '-n', '1'])
            self.add_attribute('GIT_HASH', git_hash.strip('"'))
        if os.path.isdir('.svn'):
            self.add_attribute('SUBVERSION', True)
        if os.path.isdir('.hg'):
            self.add_attribute('MERCURIAL', True)

        # Use a detective to gather specific system information
        if sys.platform.startswith('linux'):
            from linux_sysinfo import LinuxDetective
            detective = LinuxDetective()
        elif sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
            from win_sysinfo import WindowsDetective
            detective = WindowsDetective()
        elif sys.platform.startswith('os') or sys.platform.startswith('darwin'):
            from mac_sysinfo import MacDetective
            detective = MacDetective()
        else:
            detective = None

        if detective:
            self.sysinfo = detective.inspect()

    def __str__(self):
        st = ''
        for attr in self.attr_names:
            st = st + attr + ': ' + str(self.attributes[attr]) + '\n'
        return st

    def add_attribute(self,key,value):
        self.attr_names.append(key)
        self.attributes[key] = value

    def add_user_attribute(self,key,value):
        index = self.attr_names.index('PLATFORM')
        self.attr_names.insert(key)
        self.attributes[key] = value

    def append_attributes(self,extra_attributes):
        for attr in extra_attributes:
            self.add_attribute(attr[0],attr[1])

    def get_attribute(self,key):
        if self.attribute_exists(key):
            return self.attributes[key]
        else:
            return None

    def attribute_exists(self,key):
        try:
            self.attributes[key]
            return True
        except NameError:
            return False

    def write_to_file(self,filename='system_info.txt'):
        fout = open(filename, 'w')
        fout.write(self.__str__())
        fout.close()

def main(argc,argv):
    si = SystemInspector()
    si.write_to_file()
    print si

if __name__ == '__main__':
    argc = len(sys.argv)
    sys.exit(main(argc,sys.argv))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
