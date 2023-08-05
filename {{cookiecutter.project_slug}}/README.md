<h1 align="center">
    <img src="resources/img/{{cookiecutter.project_name}}.png" alt="Space Ship" width="128">
    <div align="center">{{cookiecutter.project_name}}</div>
</h1>

{{cookiecutter.project_short_description}}

## Setup
This is a simple template for a python project with a pygame app setup.
Create the environment with:

```bash
conda env create -f environment.yml
# or
conda env create -f environment.yml -n {{cookiecutter.project_slug}}
# or create a new environment with .venv
python -m venv .venv
pip install -r requirements.txt
python activate .venv/bin/activate  # or .venv\Scripts\activate.bat on windows
```

----
## [License](LICENSE.md)
This project is licensed under the terms of the [{{cookiecutter.open_source_license}}](LICENSE.md).
