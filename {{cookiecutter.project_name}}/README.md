# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

* [GitHub](https://github.com/{{ cookiecutter.github_repo_owner }}/{{ cookiecutter.project_name }})
* MIT License

## Description

## Installation

1. Clone the repository:

```bash
git clone git@github.com:{{ cookiecutter.github_repo_owner }}/{{ cookiecutter.project_name }}.git
```

2. Install [pixi](https://pixi.prefix.dev/latest/installation/)

3. Install the package

```bash
pixi run install
```

4. Activate the pixi shell

```bash
pixi shell
```

## Usage

To see available options and commands, run:

```bash
{{cookiecutter.import_name}} -h
```

## Author

{{ cookiecutter.project_name }} was created in {% now 'local', '%Y' %} by {{ cookiecutter.full_name }}.