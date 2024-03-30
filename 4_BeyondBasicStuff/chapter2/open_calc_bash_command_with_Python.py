import subprocess
print("When we use the subprocess module in Python to run a bash command, Python sends the command to the system "
      "shell, ")
print("which then executes the command and returns the output back to Python. This process allows us to use the power ")
print("of bash commands within our Python scripts. Real-World Applications of Running Bash Commands in Python. ")
print("Running bash commands in Python is not just an academic exercise. It has practical applications in a variety")
print("of domains, from automating repetitive tasks to managing system processes.")
result = subprocess.run(['open', '-a', 'calculator'])
print("\nHere's how to open calculator on Mac:", result)

print("Using zsh command will be just a command: open -a calculator")