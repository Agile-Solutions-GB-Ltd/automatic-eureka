import click
import pkg_resources

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, help='CLI provisioning commands for managing cloud platforms')
def cli() -> int:
    pass


@cli.command()
def version():
    """Display the current version."""
    click.echo(pkg_resources.get_distribution('agileetc').version)


if __name__ == '__main__':
    exit(cli())
