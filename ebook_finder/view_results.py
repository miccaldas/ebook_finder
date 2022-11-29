"""
Views the information culled from the Scrapy spider.
"""
import re
import sys

import pyfiglet
import snoop
from blessed import Terminal
from scraper.pdfdrive.clean import clean
from search_web import search_web
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def view_results():
    """
    We use Blessed to present the results and add
    a question, if the user wants to research
    further one of the results.
    """
    term = Terminal()

    data = clean()

    fig = pyfiglet.Figlet(font="larry3d")
    print(term.home + term.clear, end="")
    print(term.move_down(1) + term.paleturquoise4(fig.renderText(" ebooks")), end="")

    for i in range(len(data)):
        print(term.move_right(9) + term.bold_lavenderblush2(f"{data[i][0][0]} - {data[i][0][1]}"))
        print(term.move_right(9) + term.bold_cadetblue4(f"{data[i][1]}\n"))

    print("\n")
    web_query = input(term.move_right(9) + term.bold_lavenderblush2("(++) - Research a book: "))
    if web_query == "":
        sys.exit()
    title = data[int(web_query)][0][1]

    search_web(title)


if __name__ == "__main__":
    view_results()
