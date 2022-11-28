"""Module Docstring"""
import re

import pyfiglet
import snoop
from blessed import Terminal
from scrapy.pdfdrive.clean import clean
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def view_results():
    """"""
    data = clean()

    for i in data:
        if i["title"] == " ":
            exp = "https://www.pdfdrive.com/(.+)-e.+\.html"
            snip = re.findall(exp, i["link"])
            snip_str = snip[0]
            snip_space = snip_str.replace("-", " ")
            new_title = snip_space.title()
            i["title"] = new_title

    print(data)


if __name__ == "__main__":
    view_results()
