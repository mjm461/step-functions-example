import os
import sys
import glob
import shutil


new_step, new_class = sys.argv[1], sys.argv[2]
shutil.copytree('template', new_step)

new_step_src = os.path.join(new_step, 'src')
shutil.move(os.path.join(new_step_src, 'template'), os.path.join(new_step_src, new_step))
shutil.move(os.path.join(new_step_src, new_step, 'template.py'), os.path.join(new_step_src, new_step, new_step + '.py'))

for filename in [f for f in glob.glob(new_step + "/**", recursive=True)]:
    if os.path.isfile(filename):
        with open(filename, 'r') as fin:
            filedata = fin.read()

        filedata = filedata.replace('PACKAGE_TEMPLATE_REPLACE', new_step)
        filedata = filedata.replace('CLASS_TEMPLATE_REPLACE', new_class)

        with open(filename, 'w') as file:
            file.write(filedata)
