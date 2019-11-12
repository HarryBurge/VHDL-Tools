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
    """
    Control structure for compilation of a file passed

    :param string path: Path of the file to be compiled
    :param string file_to_be_compiled: Name of the file to be compiled
    :param string output_compiled_file: Name of the output file

    :returns None
    """

    # Open, read and close file_to_be_compiled
    file = open(path + '\\' + file_to_be_compiled, 'r')
    VHDLText = file.read()
    file.close()

    # Remove tabs and split into lines
    VHDLText = VHDLText.replace('    ','') .replace('\t','').split('\n')

    # Remove comments
    VHDLText = removeComments(array_of_lines=VHDLText,comment_identifiers=['--','#','//'])

    print(VHDLText)


def removeComments(array_of_lines, comment_identifiers):
    """
    Removes all of a line after a certain identifier including itself

    :param [string, ...] array_of_lines: An array of lines
    :param [string, ...] comment_identifiers: An array of the comment identifiers

    :returns [string, ...]: array_of_lines minus the comments
    """

    temp = []

    for line in array_of_lines:
        for symbol in comment_identifiers:

            # If line has a comment
            if line.find(symbol) != -1:
                # Remove it and everything after it
                line = line[:line.find(symbol)]

        temp.append(line)

    return temp
