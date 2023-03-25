import glob
import re
import version 
import os

v = version.__version__.replace('.','_')

read_files = glob.glob("mirthpy\mirthpy\*.py")
read_files.remove('mirthpy\\mirthpy\\__init__.py')

imports = {}
for f in read_files:
    with open(f, "r") as infile:
        for line in infile.readlines():
            if line.startswith('from .'):
                imp = line.replace('from .','')
                imp = re.sub(" import.+\n","",imp) + '.py'
                if f not in imports.keys():
                    imports[f] = []

                imports[f].append(f"mirthpy\\mirthpy\\{imp}")

withDeps = set([i for i in imports.keys()])
orderedImports = [f for f in read_files if f not in withDeps]

while len(orderedImports) < len(read_files):
    for key, items in list(imports.items()):
        if len(items) == 0: continue
        if key not in orderedImports and set(items).issubset(orderedImports):
            print(f"added {key}")
            orderedImports.append(key)
            del imports[key]

if not os.path.exists(f"mirthpy\\build\\{v}"):
    os.mkdir(f'mirthpy\\build\\{v}')

importPackages = []
with open(f"mirthpy\\build\\{v}\\mirthpy.py", "w") as outfile:
    for f in orderedImports:
        with open(f, "r") as infile:
            for line in infile.readlines():
                # clear local imports
                if not re.search("from \..+\n",line):
                    if (re.search("from .+\n", line) or re.search("import .+\n",line)) and '=' not in line:
                        importPackages.append(line)
                    else:
                        outfile.write(line)
            #outfile.write('\n'+re.sub("from \..+\n","",infile.read()))


fileToWrite = f"mirthpy\\build\\{v}\\mirthpy.py"
with open(fileToWrite, "r+") as outfile:
    content = outfile.read()
    outfile.seek(0,0)
    outfile.write("".join(set(importPackages))+f"\n# mirthpy - {version.__version__}\n\n# Description: {version.__description__}\n"+content)
    
print(f"Combined classes in file: {fileToWrite}")