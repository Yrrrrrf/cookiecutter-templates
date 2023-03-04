import os
import sys


# Colors
OK_COLOR = '\033[1;32m'  # Green
ERROR_COLOR = '\033[1;31m'  # Red
RESET_COLOR = '\033[0m'  # Reset

# Project name
project_name = '{{cookiecutter.project_name}}'


# Check if the project name is valid
if not project_name.isidentifier():  # Check if the project name is a valid Python identifier
    print(f'{ERROR_COLOR}ERROR: The project name ({project_name}) is not a valid Python identifier!{RESET_COLOR}')  # Exit to cancel project
    sys.exit(1)  # Exit to cancel project

reserved_names = ['test', 'tests', 'doc', 'docs', 'sample', 'samples', 'example', 'examples']
if project_name.lower() in reserved_names:  # Check if the project name is a reserved name
    print(f'{ERROR_COLOR}ERROR: The project name ({project_name}) is a reserved name!{RESET_COLOR}')  # Exit to cancel project
    sys.exit(1)  # Exit to cancel project

print(f'{OK_COLOR}Project name is valid!{RESET_COLOR}')
print(f'Creating project "{project_name}" at "{os.getcwd()}"')

