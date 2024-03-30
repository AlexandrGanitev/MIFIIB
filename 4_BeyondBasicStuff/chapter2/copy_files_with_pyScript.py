import subprocess

procObj = subprocess.run(['cp', 'text.py', 'TestDirectory'])

print("The file has been copied with the Python script. "
      "The shell command completed, the text.py file found in the "
      "specially created subdirectory 'TestDirectory'")