# cookiecutter-flask-basic

A minimal Flask template for [cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Features

- Supports python ≥ 3.6
- Uses the [poetry](https://github.com/python-poetry/poetry) dependency manager by default
- (Optional) Flask environment variable configuration using `python-dotenv`
- (Optional) Setup and initialize version control system
- (Optional) Include files necessary for deployment to Heroku

## Usage

### Requirements

This template requires [cookiecutter](https://github.com/cookiecutter/cookiecutter) and [poetry](https://github.com/python-poetry/poetry). These can be simply installed using `pip`

```bash
$ pip install --user cookiecutter poetry
```

### Create a project

You can use `cookiecutter` to create a new project based on this template. You will be prompted to provide some details that will be used to setup the project.

```bash
$ cookiecutter gh:ang3orge/cookiecutter-flask-basic
```

### Install dependencies

The basic structure of the project is now ready. Use the `poetry` tool to install all dependencies in a virtual environment

```bash
$ cd project_name
$ poetry install
```

You are now ready to start building your flask app
