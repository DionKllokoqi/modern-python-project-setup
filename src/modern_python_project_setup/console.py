"""Console script for modern_python_project_setup.
"""

import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """Modern Python library"""
    click.echo("Hello, world!")
