"""
Cleans output of Scrapy's spider.
"""
import json

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def clean():
    """
    Just added the head of the url, so as
    to have the complete link.
    """
    with open("/home/mic/python/ebook_finder/ebook_finder/scrapy/pdfdrive/results.json") as f:
        data = json.load(f)

    for i in data:
        i["link"] = f'https://www.pdfdrive.com{i["link"]}'

    return data


if __name__ == "__main__":
    clean()
