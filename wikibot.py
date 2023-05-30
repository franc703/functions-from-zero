import click
from mylib.bot import scrape


@click.command()
@click.option(
    "--name", prompt="Wikipedia page to scrape", help="Webpage we want to scrape"
)
@click.option("--length", help="The length of the output from Wikipedia")
def cli(name, length):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}:", bg="blue", fg="white"))


if __name__ == "__main__":
    cli()
