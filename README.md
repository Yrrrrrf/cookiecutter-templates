# cookiecutter - App

This is a cookiecutter template for creating a new app using [python](https://www.python.org/) & [js](https://www.javascript.com/).

### Create App Template
```
cookiecutter https://github.com/Yrrrrrf/cookiecutter-templates --checkout app
```

### Generated Project Structure
```
│   .gitignore
│   environment.yml
│   LICENSE.md
│   README.md
│   requirements.txt
├───logs
│       project_name.ipynb
├───resources
│   ├───audio
│   ├───img
│   ├───temp
│   └───video
├───src
│   │   main.py
│   ├───app
│   │   ├───components
│   │   │   ├───interface
│   │   │   └───logic
│   │   └───web
│   │       │   index.html
│   │       ├───api
│   │       │   ├───controller
│   │       │   ├───model
│   │       │   └───service
│   │       └───view
│   │           ├───css
│   │           └───html
│   ├───config
│   └───data
└───test
```