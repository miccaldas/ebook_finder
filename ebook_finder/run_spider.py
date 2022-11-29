"""
Creates the Scrapy spider.
"""

import subprocess

import snoop

from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def run_spider():
    """
    We use Subprocess to call the Scrapy
    command that generates a spider.
    """

    cmd = "scrapy crawl pdf -O results.json"
    path = "/home/mic/python/ebook_finder/ebook_finder/scraper/pdfdrive"
    subprocess.run(cmd, cwd=path, shell=True)


if __name__ == "__main__":
    run_spider()
