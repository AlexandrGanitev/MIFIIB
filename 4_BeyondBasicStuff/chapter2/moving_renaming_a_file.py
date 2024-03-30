import subprocess

renamed_file = subprocess.run(['mv', 'text.py', 'renamedFile.py'])
procObj = subprocess.run(['ls', '-al'])
print("The file has been renamed, here's an updated list of files: ", renamed_file, procObj)

"""
al@ubuntu:~/someFolder$ mv hello.py goodbye.py
"""
