import click
import pkg_resources

from src.agileetc.sample import read, pretty

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, help='CLI provisioning commands for managing cloud platforms')
def cli() -> int:
    pass


@cli.command()
def version() -> None:
    """Display the current version."""
    click.echo(pkg_resources.get_distribution("agileetc").version)


@cli.command()
@click.argument('data_path', type=click.Path(exists=True))
def print_sample(data_path) -> None:
    """Print sample data using poetry run agileetc print-sample ."""
    data = read(data_path)
    pretty(data)


if __name__ == '__main__':
    exit(cli())
