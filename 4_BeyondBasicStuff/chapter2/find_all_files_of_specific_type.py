import subprocess, locale

procObj = subprocess.run(['find', '.', '-name', "*.py"], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getlocale()[1])
print(outputStr)

"""
The original command in the shell will be: al@ubuntu:~/Desktop$ find . -name "*.py"
So here we divide each word of the command and its parameters and put them in quotes.
"""