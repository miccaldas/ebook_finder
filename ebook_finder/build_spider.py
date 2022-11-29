"""
Builds Scrapy spider from user input.
"""
import click
import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def build_spider(url):
    """
    Asks for a query to the user, inserts it
    on a search url and recreates the spider
    file.
    """

    lowercase = url.lower()
    next_page = f"https://pdfdrive.com/search?q={lowercase}&page=2"
    url_append = lowercase.replace(" ", "+")
    start_url = f"https://www.pdfdrive.com/search?q={url_append}"

    with open("/home/mic/python/ebook_finder/ebook_finder/scraper/pdfdrive/pdfdrive/spiders/pdf.py", "w") as f:
        f.write("import scrapy\n")
        f.write("from pdfdrive.items import PdfdriveItem\n")
        f.write("import snoop\n")
        f.write("from snoop import pp\n\n\n")
        f.write("class PdfSpider(scrapy.Spider):\n")
        f.write("    name = 'pdf'\n")
        f.write("    allowed_domains = ['www.pdfdrive.com']\n")
        f.write(f"    start_urls = ['{start_url}', '{next_page}']\n\n")
        f.write("    @snoop\n")
        f.write("    def parse(self, response):\n")
        f.write("        pd = PdfdriveItem()\n")
        f.write("        pd['link'] = response.xpath('//div[@class=\"file-right\"]/a/@href').getall()\n")
        f.write("        return pd")


if __name__ == "__main__":
    build_spider()
