


from os import listdir
from os.path import isfile, join
from os import rename, chdir
from os import walk

import numbers

mypath = "arbetsformedlingen_pdf/"

files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    break

chdir(mypath)

for file in files:
    print ("trying " + file)
    name_parts = file.split(".")
    if (len(name_parts) > 2):
        if name_parts[2].isdigit:
            new_parts = []
            new_parts.append (name_parts[0])
            new_parts.append (name_parts[2])
            new_parts.append (name_parts[1])
            new_file = ".".join (new_parts)
            print ("moving " + file + " to " + new_file)
            rename (file, new_file)