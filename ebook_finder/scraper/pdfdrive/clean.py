"""
Cleans output of Scrapy's spider.
"""
import json
import re

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def clean():
    """
    As it's only one field, the dictionary that Scrapy
    returns it's too much for what we need. The first
    part is dedicated to convert it to a list and, as
    it was already inside another list, flatten it.
    We add the head of the url to the Scrapy results,
    put them in a list and create another where we
    create titles from the url strings. So as to be
    able to choose books from the list, we enumerate
    the titles, so we can use the numbers as id.
    Finally we join the two lists in a list of lists.
    """
    with open("/home/mic/python/ebook_finder/ebook_finder/scraper/pdfdrive/results.json") as f:
        data = json.load(f)

    partial_lst = []
    flat_lst = []
    for i in data:
        partial_lst.append(i["link"])
    for sub in partial_lst:
        for item in sub:
            flat_lst.append(item)

    url_lst = [f"https://www.pdfdrive.com{i}" for i in flat_lst]

    title_lst = []
    for i in url_lst:
        exp = "https://www.pdfdrive.com/(.+)-e.+\.html"
        snip = re.findall(exp, i)
        snip_str = snip[0]
        snip_space = snip_str.replace("-", " ")
        new_title = snip_space.title()
        title_lst.append(new_title)

    title_enum = [i for i in enumerate(title_lst)]
    print(title_enum)

    final_lst = []
    for t, u in zip(title_enum, url_lst):
        item = [t, u]
        final_lst.append(item)

    return final_lst


if __name__ == "__main__":
    clean()
