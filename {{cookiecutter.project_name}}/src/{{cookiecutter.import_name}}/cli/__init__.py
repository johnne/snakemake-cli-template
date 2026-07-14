from pathlib import Path

from snk_cli import CLI

{{cookiecutter.import_name}} = CLI(Path(__file__).parent.parent)
