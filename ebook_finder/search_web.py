"""
Copy of the 'text_browser/search' module.
Didn't imported it directly because I
fucked up its setup.py
"""
import re
import sys

import pyfiglet
import snoop
from blessed import Terminal
from ScrapeSearchEngine.ScrapeSearchEngine import Bing, Google, Startpage
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def search_web(srch_query):
    """
    Function is called from the 'view_results' module.
    It returns web links to a given query of a book.
    """
    term = Terminal()
    userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

    startpage = Startpage(srch_query, userAgent)
    google = Google(srch_query, userAgent)
    bing = Bing(srch_query, userAgent)

    hrefs = []
    for lnk in startpage:
        hrefs.append(lnk)
    for link in google:
        hrefs.append(link)
    for lk in bing:
        hrefs.append(lk)

    p = re.compile("\"|'")
    quote_marks = []

    for i in hrefs:
        sane = p.sub("", i)
        quote_marks.append(sane)

    print(quote_marks)

    href_set = set(quote_marks)

    results = [i for i in enumerate(href_set)]

    fig = pyfiglet.Figlet(font="larry3d")
    print(term.home + term.clear, end="")
    print(term.move_down(1) + term.salmon1(fig.renderText(" search")), end="")

    for result in href_set:
        print(term.move_right(9) + term.bold_peachpuff(str(result)))


if __name__ == "__main__":
    search_web()
