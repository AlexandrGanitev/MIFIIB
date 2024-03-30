import subprocess

renamed_file = subprocess.run(['mv', 'text.py', 'renamedFile.py'])
procObj = subprocess.run(['ls', '-al'])
print("The file has been renamed, here's the CompletedProcess data: ", renamed_file, procObj)

"""
The script renames one file and gives it another name:
al@ubuntu:~/someFolder$ mv text.py renamedFile.py
"""
