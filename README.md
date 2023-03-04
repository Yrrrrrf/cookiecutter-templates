# Rust App Template

This template is thinked for create a Rust App with a simple structure.

It includes a directory structure that allow you to organize your project in a way that is easy to understand and maintain.

## Create App Template
```
cookiecutter https://github.com/Yrrrrrf/cookiecutter-templates --checkout rust_app
```

## Generated Project Structure
```bash
project_name/  # root directory
│   .gitignore
│   LICENSE.md  # https://choosealicense.com/
│   README.md  # this file
│   Cargo.toml  # cargo configuration file
├───resources/  # resources directory
│   └───img/  # images directory
└───src/  # source code directory
    ├───main.rs  # main file
    ├───main_dev.rs  # dev main file
    ├───components/  # app components
    ├───config/  # global configuration
    │   └───globals.rs  # global configuration file
    └───util/  # util modules
        └───terminal.rs  # terminal util module
```

