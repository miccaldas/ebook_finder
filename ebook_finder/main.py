"""Main module of the app."""
import click
import snoop
from build_spider import build_spider
from run_spider import run_spider
from snoop import pp
from view_results import view_results


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.option("-q", "--query", prompt=True)
@snoop
def main(query):
    """
    We ask the user what is his query and
    call all the apropriate modules.
    """

    build_spider(query)
    run_spider()
    view_results()


if __name__ == "__main__":
    main()
