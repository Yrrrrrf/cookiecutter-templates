import subprocess  # allow to run shell commands


# colors
OK_COLOR = '\033[1;32m'  # green
RESET_COLOR = '\033[0m'  # reset

# variables
license: str = '{{cookiecutter.open_source_license}}'


def _get_license(license: str) -> str:
    '''
    Use Xpath to get the license text from the choosealicense.com

    Param:
    ----
        license: license name
    '''
    # todo: implement this function
    return 'xd'


def main():
    '''
    Entry point of the script.
    '''
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


if __name__ == '__main__':
    '''
    This is the entry point of the script.
    '''
    main()

