import os
import sys
import glob
import fileinput
import shutil


new_step = sys.argv[1]

#shutil.copytree('template', new_step)
#shutil.move(
#    os.path.join(new_step, 'src', 'template'),
#    os.path.join(new_step, 'src', 'new_step')
#)

files = [f for f in glob.glob(new_step + "/**", recursive=True)]

for f in files:
    print(f)

#with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
#    for line in file:
#        print(line.replace(text_to_search, replacement_text), end='')
