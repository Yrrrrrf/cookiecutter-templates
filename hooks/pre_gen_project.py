import os
import sys

OK_COLOR = '\033[1;32m'  # Green
ERROR_COLOR = '\033[1;31m'  # Red
RESET_COLOR = '\033[0m'  # Reset

project_name = '{{ cookiecutter.project_name }}'

# Check if the project name is valid
if not project_name.isidentifier():  # Check if the project name is a valid Python identifier
    print(f'{ERROR_COLOR}ERROR: The project name ({project_name}) is not a valid Python identifier!{RESET_COLOR}')
    sys.exit(1)  # Exit to cancel project

reserved_names = ['test', 'tests', 'docs', 'examples', 'sample', 'samples', 'example', 'example']
if project_name.lower() in reserved_names:  # Check if the project name is a reserved name
    # using f-strings
    print(f'{ERROR_COLOR}ERROR: The project name ({project_name}) is a reserved name!{RESET_COLOR}')
    sys.exit(1)  # Exit to cancel project

print(f'{OK_COLOR}Project name is valid!{RESET_COLOR}')
print(f'Creating project "{project_name}" at "{os.getcwd()}"')

