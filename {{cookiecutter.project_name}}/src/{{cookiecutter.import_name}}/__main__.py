# SPDX-FileCopyrightText: {% now 'local', '%Y' %}-present {{cookiecutter.full_name}} <{{cookiecutter.email}}>
#
# SPDX-License-Identifier: MIT
#
# When using this template, replace 'project' with the name of the project

import sys

if __name__ == "__main__":
    from {{cookiecutter.import_name}}.cli import {{cookiecutter.import_name}}

    sys.exit({{cookiecutter.import_name}}())
