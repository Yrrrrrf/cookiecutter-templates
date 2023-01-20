import subprocess  # allow to run shell commands


OK_COLOR = '\033[1;32m'  # Green
RESET_COLOR = '\033[0m'  # Reset


# create .venv folder and activate it
subprocess.run(['python', '-m', 'venv', '.venv'])
subprocess.run(['source', '.venv\\Scripts\\activate'])  # bash
# subprocess.run(['.venv\\Scripts\\activate.ps1'])  # powershell

# dependencies
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])  # read the requirements.txt file and install the dependencies
subprocess.run(['find', '.', '-name', '*.gitkeep', '-delete'])  # find all .gitkeep files and delete them

# repository
subprocess.run(['git', 'init'])  # initialize the repository
subprocess.run(['git', 'add', '*'])  # add all files
subprocess.run(['git', 'commit', '-m', 'Initial commit'])  # commit the changes

# print confirmation message
print(f'{OK_COLOR}Project generated properly!{RESET_COLOR}')
