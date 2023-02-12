# cookiecutter templates

This repository contains a collection of cookiecutter templates for various projects.

### Create App Template
```
cookiecutter https://github.com/Yrrrrrf/cookiecutter-templates --checkout data_science
```

### Generated Project Structure
```bash
project_name/  # root directory
│   .gitignore
│   LICENSE.md  # https://choosealicense.com/
│   README.md  # this file
│   requirements.txt  # pip freeze > requirements.txt
├───data/  # data files (not to be committed to git)
│   ├───raw/  # raw data files
│   └───processed/  # processed data files
├───src/  # source files
│   ├───config/  # config files
│   └───main.py  # main entry point
├───notebooks/  # jupyter notebooks (exploratory analysis, etc.)
├───reports/  # reports (final reports, presentations, etc.)
└───tests/  # tests (unit, functional, etc.)
```
