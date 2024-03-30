import subprocess, locale
procObj = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getlocale()[1])
print(outputStr)

"""
We pass the ['ls', '-al'] list to subprocess.run()
1. This list contains the
command name ls, followed by its arguments, as individual strings. Note
that passing ['ls –al'] wouldn’t work. We store the command’s output as a
string in outputStr 
2. Online documentation for subprocess.run() and locale.
getdefaultlocale() will give you a better idea of how these functions work, but
they make the code work on any operating system running Python."""