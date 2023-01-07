import subprocess  # allow to run shell commands


OK_COLOR = '\033[1;32m'  # Green
RESET_COLOR = '\033[0m'  # Reset

# install the dependencies
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
subprocess.run(['conda', 'env', 'create', '-f', 'environment.yml'])
# create the initial commit
subprocess.run(['git', 'init'])
subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', 'Initial commit'])

print(f'{OK_COLOR}Project generated properly!{RESET_COLOR}')
