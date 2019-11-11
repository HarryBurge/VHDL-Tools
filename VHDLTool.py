# Documentation string of this module
"""
This is the control structure for using the VHDL tools. This module provides these options:

-> Compile VHDL into Python
-> Waveform creation
-> Debugger

"""
# Informational variables
__author__    = "$Author: HarryBurge $"
__version__   = "$Revision: 1 $"
__date__      = "$Date: 2019-11-08 11:42:00 $"

#----------------------------- actual code --------------------------------


# Imports
import sys
import os
import lib.compiler as compiler


# Main
def main(path,args):
    
    # Args interpretation
    if args[1] in ('-C','-c','C','c'): #Compile option

        # Args validation
        if len(args) in range(3,5):
            # Check VHDL file exists
            if os.path.isfile(args[2]):
                # Run compiler with config
                if len(args)==3: compiler.compile(path=path,file_to_be_compiled=args[2])
                if len(args)==4: compiler.compile(path=path,file_to_be_compiled=args[2], output_compiled_file=args[3])
            # VHDL file doesn't exist - Error
            else:
                raise FileNotFoundError(f'''
                {args[2]} is not found
                ''')
        # To many or to little arguments - Error
        else:
            raise ValueError(f'''
            There are {len(args) - 2} args.
            Format should be "-c <File_To_Be_Compiled> (*.txt) [<Output_Compiled_File> (*.py) | compiledVHDL.py]"
            ''')


    elif args[1] in ('-W','-w','W','w'): # Waveform read option
        # TODO: Create a waveform function
        print("1")


    elif args[1] in ('-D','-d','D','d'): # Simulate option
        # TODO: Create a debugger
        print("1")


    elif args[1] in ('--Help','--help','-Help','-help','Help','help','-hlp','hlp'):
        # TODO: Create help info
        print("help string")


    else: # Invalid first option
        raise ValueError(f'''
        Invalid argument passed -> {args[1]}
        Choices are:
        -c <File_To_Be_Compiled> (*.txt) [<Output_Compiled_File> (*.py) | compiledVHDL.py]
        -w <File_Compiled> (*.py) <File_Inputs> (*.txt)
        -d <File_Compiled> (*.py) [<File_Inputs> (*.txt) | ]
        ''')
