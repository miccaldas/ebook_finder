"""
Builds Scrapy spider from user input.
"""
import click
import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.option("-u", "--url", prompt=True)
@snoop
def build_spider(url):
    """
    Asks for a query to the user, inserts it
    on a search url and recreates the spider
    file.
    """

    lowercase = url.lower()
    url_append = lowercase.replace(" ", "+")
    start_url = f"https://www.pdfdrive.com/search?q={url_append}"

    with open("scrapy/pdfdrive/pdfdrive/spiders/pdf.py", "w") as f:
        f.write("import scrapy\n")
        f.write("import snoop\n\n")
        f.write("from snoop import pp\n\n\n")
        f.write("class PdfSpider(scrapy.Spider):\n")
        f.write("    name = 'pdf'\n")
        f.write("    allowed_domains = ['www.pdfdrive.com']\n")
        f.write(f"    start_urls = ['{start_url}']\n\n")
        f.write("    @snoop\n")
        f.write("    def parse(self, response):\n")
        f.write("        title = response.xpath('//h2/text()').getall()\n")
        f.write("        link = response.xpath('//div[@class=\"file-right\"]/a/@href').getall()\n\n")
        f.write("        for item in zip(title, link):\n")
        f.write("            results = {\n")
        f.write("                'title': item[0],\n")
        f.write("                'link': item[1],\n")
        f.write("            }\n")
        f.write("            yield results")


if __name__ == "__main__":
    build_spider()
