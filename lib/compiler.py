# Documentation string of this module
"""
This module compilers a VHDL text file into a Python file which can be ran using VHDL-Tools.
"""
# Informational variables
__author__    = "$Author: HarryBurge $"
__version__   = "$Revision: 1 $"
__date__      = "$Date: 2019-11-11 09:52:00 $"

#----------------------------- actual code --------------------------------

# Imports
import sys
import os

def compile(path, file_to_be_compiled, output_compiled_file='compiledVHDL.py'):

    file = open(path + '\\' + file_to_be_compiled, 'r')
    VHDLText = file.read()
    file.close()

    VHDLText = VHDLText.replace('    ','') .replace('\t','').split('\n')

    VHDLText = removeComments(VHDLText, ['--','#','//',"'"])

    print(VHDLText)

def removeComments(array_of_lines, comment_identifiers)
