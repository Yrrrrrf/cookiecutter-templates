# Rust App Template

This template is thinked for create a PyGame App with a simple structure.

It includes a directory structure that allow you to organize your project in a way that is easy to understand and maintain.

## Create App Template
```bash
cookiecutter https://github.com/Yrrrrrf/cookiecutter-templates --checkout pygame_app
```

## Generated Project Structure
```bash
project_name/  # root directory
│   .gitignore
│   LICENSE.md  # https://choosealicense.com/
│   README.md  # this file
├───resources/  # resources directory
│   └───img/  # images directory
│   └───data/  # data directory
└───src/  # source code directory
    ├───main.py  # main file
    ├───components/  # app components
    │   └───app.py  # app component (window management)
    │   └───editor.py  # main event loop component
    ├───config/  # app components
    │   └───globals.py  # global configuration file
```

