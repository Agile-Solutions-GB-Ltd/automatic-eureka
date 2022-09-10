import os
from pathlib import Path

import click
import yaml
from prettytable import PrettyTable

from src.agileetc.terminal import print_cross_message


def path(location) -> Path:
    """Gets sample file."""
    return Path(os.path.join(location, 'data', 'sample.yml'))


def read(location) -> str:
    """Reads sample file."""
    click.secho(f"Using data location {location}", fg='blue')
    file = path(location)
    if not file.is_file():
        print_cross_message(f"File {file} not found!", True)
    else:
        with open(file, 'r') as f:
            return yaml.safe_load(f)


def pretty(data) -> None:
    table = PrettyTable()
    table.field_names = ['Name', 'Description', 'Message']
    for entry in data:
        table.add_row([entry['name'], entry['description'], entry['message']])
    click.secho(table, fg='blue')
