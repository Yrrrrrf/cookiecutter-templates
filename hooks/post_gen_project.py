import subprocess  # allow to run shell commands
import asyncio  # async programming
import datetime  # get the current date and time

import httpx  # async http client
from bs4 import BeautifulSoup  # parse html


# colors
OK_COLOR = '\033[1;32m'  # green
RESET_COLOR = '\033[0m'  # reset

author: str = '{{cookiecutter.author_name}}'
license: str = '{{cookiecutter.open_source_license}}'
# license: str = 'MIT License'
# license: str = 'GPL v3'

license_link = {  # links to the licenses on the choosealicense.com
    'MIT License': 'mit/',  # todo: replace year and name in the license
    'BSD License': 'bsd-3-clause/',
    'GPL v3': 'gpl-3.0/',
    'Apache 2.0': 'apache-2.0/'
}


async def __get_license(license_url: str) -> str:
    '''
    Use Xpath to get the license text from the choosealicense.com

    Param:
    ----
        license: license name
    '''
    async with httpx.AsyncClient() as client:  # Use the async client to get the response
        response = await client.get(license_url)  # get the response from the url
        if response.status_code == 200:  # check if the response is ok
            print(f'License obtained successfully: {response.status_code}')  # print the status code
            license_text = BeautifulSoup(response.text, 'html.parser').find('pre', id='license-text')  # parse the html and get the $x('//pre[@id="license-text"]/text()') text
            license_text = str(license_text).split('>')[1].replace('&lt;', '<').replace('&gt;', '>').replace('</pre', '')  # remove the html tags
            license_text = license_text.replace('year', f'{datetime.datetime.now().year}').replace('fullname', f'{author}').replace('name of author', f'{author}')  # replace the placeholders with the author name and the current year
        else: raise Exception(f'Error: {response.status_code}')  # raise an exception if the response is not ok

    with open('LICENSE.md', 'w') as file:  # write the license text to a file
        file.write(str(license_text))
    print(license_text)

    return license_text  # return the license text


def main() -> None:
    '''
    Entry point of the script.
    Create the virtual environment, install the dependencies, initialize the repository and delete the .gitkeep files.
    '''
    # create .venv folder and activate it
    subprocess.run(['python', '-m', 'venv', '.venv'])
    subprocess.run(['source', '.venv\\Scripts\\activate'])  # bash
    # subprocess.run(['pip', 'install', '--upgrade', 'pip'])  # upgrade pip
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
    # main()

    license_url = 'https://choosealicense.com/licenses/' + license_link[license]  # get the license url

    asyncio.run(__get_license(license_url))  # run the main function
