# rename_files
rename_files.py renames files in batch in the current working directory or recursively. It does not rename one file at a time.

Rename files in a directory in batch

    rename.py -f[--from] "'" -t[--to] "" -d[--directory] /home/someone/Pictures

    Options:

    -f|--from        The string that is to be changed in the filename
    -t|--to          The string that will replace the string in -f|--from
    -d|--directory   The directory path that the files are in
    -r|--recurse     Recurses through the subdirectories in -d|--directory
