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
import re
import multiprocessing


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

    # Put all entitys into a pool and have them then be compiled into python then sent back to possible a index

    # Flatten VHDLText # TODO: Make multiprocessed
    temp = ''
    for line in VHDLText:
        temp += line
    VHDLText = temp

    # Splits up all sections
    VHDLText = re.split('end entity;|end architecture;', VHDLText)

    # Splits up architectures from entitys # TODO: Make multiprocessed
    entitys = []
    architectures = []

    for line in VHDLText:
        if line.find('entity') == False:

            # Do manipulations for usable format
            line = line.replace('entity ', '')
            line = line.replace(' isport{', ';')
            line = line.replace('};', '')
            line = line.split(';')

            del line[-1]
            entitys.append(line)

        elif line.find('architecture') == False:

            # Do manipulations for usable format
            line = line.replace('architecture of ', '')
            line = line.replace(' isbegin{', ';')
            line = line.replace('};', '')
            line = line.split(';')

            del line[-1]
            architectures.append(line)

    # Combines entity with architecture to chip # TODO: Make multiprocessed
    chips = []

    for i in entitys:
        for j in architectures:
            if i[0] == j[0]:
                temp = {}

                params = []
                returns = []
                for k in i[1:]:
                    if k.split(':')[1].lstrip().split(' ')[0] == 'in':
                        params.append(k.split(':')[0].strip() + ':' + k.split(':')[1].lstrip().split(' ')[1])
                    elif k.split(':')[1].lstrip().split(' ')[0] == 'out':
                        returns.append(k.split(':')[0].strip() + ':' + k.split(':')[1].lstrip().split(' ')[1])

                logic = []
                for k in j[1:]:
                    logic.append(k)

                temp['name'] = i[0]
                temp['params'] = params
                temp['returns'] = returns
                temp['logic'] = logic

                chips.append(temp)
                break

    # Puts pre compiled content in for ease of use for users
    # file = open(os.path.dirname(os.path.abspath(__file__)) + '\\PreBuilt.py', 'r')
    # code = file.read() + '\n\n'
    # file.close()

    code = ''
    # Processes all the items # TODO: Make multiprocessed
    for i in chips:
        code += codeGeneration(i) + '\n\n'

    #print(code)




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

        # Removes blank lines
        if line != '':
            temp.append(line.rstrip().lstrip())

    # Empty check
    if temp == []:
        raise EmptyFileError(f'''
        The file to be compiled has only comments in it, or is blank
        ''')

    return temp

# TODO: Need to create the thing where you store the object of diffrent things
def codeGeneration(chip):
    """
    Takes and converts a chip into python code

    :param dict chip: Holds info for chip to be created {name, params, returns, logic}

    :returns string: Pyhton code of chip
    """

    # Header of the class
    code = 'class ' + chip.get('name') + '():\n\n'


    # Initalize output variables
    for i in chip.get('returns'):
        if i.split(':')[1] == 'std_logic':
            code += '\t' + i.split(':')[0] + ' = False\n'


    for i in chip.get('logic'):
        i = i.split('<=')
        i[0] = i[0].rstrip()
        i[1] = i[1].lstrip()

        i[1] = toTokenCode(i[1])
        if type(i[1]) == str:
            i[1] = [i[1]]

        print(i[1])
        ##Pick up from here, you need to make it so the array that comes back
        ##All the chips are created like in example PreBuilt.py -> XORs = {}
        ##Then below at somepoint actually create the logic noob


    code += '\n'


    # Init function
    code += '\tdef __init__(self'
    for i in chip.get('params'):
        if i.split(':')[1] == 'std_logic':
            code += ', ' + i.split(':')[0]
    code += '):\n'

    for i in chip.get('params'):
        if i.split(':')[1] == 'std_logic':
            code += '\t\tself.' + i.split(':')[0] + ' = ' + i.split(':')[0] + '\n'
    code += '\n'


    # Get for outputs
    code += '\t def getOutputs(self):\n'
    code += '\t\treturn {'
    for i in chip.get('returns'):
        if i.split(':')[1] == 'std_logic':
            code += '\'' + i.split(':')[0] + '\':self.' + i.split(':')[0] + ', '
    code = code[:-2] + '}\n'

    return code

def toTokenCode(logic_line):

    if logic_line.find('(') != -1:
        Command = logic_line[:logic_line.find('(')]

        logic_line = logic_line[logic_line.find('(')+1:-1]

        leftSide = logic_line[:logic_line.rfind(',')]
        rightSide = logic_line[logic_line.rfind(','):]

        return [Command, toTokenCode(leftSide), toTokenCode(rightSide)]
    return logic_line
