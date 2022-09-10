
import click
from src.agileetc import EXITCODE


def print_check_message(text) -> None:
    click.echo(b'\xE2\x9C\x94' + f' {text}'.encode())


def print_cross_message(text, leave=False) -> None:
    click.echo(b'\xE2\x9D\x8C' + f' {text}'.encode())
    if leave:
        exit(EXITCODE)
