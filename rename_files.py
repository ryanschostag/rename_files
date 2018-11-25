#! /usr/bin/python
# https://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory

import os
import sys


SEPARATOR = '\\' if sys.platform == 'win32' else '/'


def _file_list(d, recurse=False):
    # returns a file list based 
    # d: <string> directory path to start file search
    # recurse: <bool> True to recurse 
    file_list = []
    if recurse:
        for i in os.walk('.'):
            for j in i:
                 for k in j:
                     file_list.append(os.path.abspath(k))
        return file_list
    else:
        file_list.extend(os.listdir('.'))
        return file_list
   

def rename_files(replace_from, replace_to, directory='.', recurse=False):
    script_dir = SEPARATOR.join(os.path.abspath(sys.argv[0]).split(SEPARATOR)[:-1])
    os.chdir(os.path.abspath(directory))
    files = _file_list(directory, recurse=recurse)
    for file in files:
        try:
            os.rename(file, file.replace(replace_from, replace_to))
        except OSError:
            pass
    os.chdir(script_dir)


def help_message():
    return """

    {}

    Rename files in a working directory in batch.

    rename.py -f[--from] "'" -t[--to] '' -d[--directory] /home/someone/Pictures

    Options:

    -f|--from        The string that is to be changed in the filename
    -t|--to          The string that will replace the string in -f|--from
    -d|--directory   The directory path that the files are in
    -r|--recurse     Recurses through the subdirectories in -d|--directory
    
    """.format(sys.argv[0])


def rename_arg_processor():
    r_from = None
    r_to = None
    directory = None
    recurse = False
    required_args = ('-h', '--help', '-d', '--directory', '-f', '--from', '-t', '--to', '-r', '--recurse')

    valid_arg_count = 0
    for a in required_args:
        for position, arg in enumerate(sys.argv):
            if a == arg.lower():
                valid_arg_count += 1

    if valid_arg_count == 0:
        print(help_message())
        raise SyntaxError('{} requires at least one argument'.format(sys.argv[0]))

    for index, arg in enumerate(sys.argv):
        if arg.lower() == '-h' or arg.lower() == '--help':
            print(help_message())
            exit()
        if arg.lower() == '-d' or arg.lower() == '--directory':
            directory = sys.argv[index+1]
            if not os.path.isdir(directory):
                print(help_message())
                raise ValueError('Directory not valid')
        if arg.lower() == '-f' or arg.lower() == '--from':
            r_from = sys.argv[index+1]
        if arg.lower() == '-t' or arg.lower() == '--to':
            r_to = sys.argv[index+1]
        if arg.lower() == '-r' or arg.lower() == '--recurse':
            recurse = True
            
    return r_from, r_to, directory, recurse


def main():
    replace_from, replace_to, directory, recurse = rename_arg_processor()
    rename_files(replace_from=replace_from, replace_to=replace_to, directory=directory, recurse=recurse)


if __name__=="__main__":
    main()

