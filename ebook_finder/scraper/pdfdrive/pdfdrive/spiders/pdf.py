import scrapy
from pdfdrive.items import PdfdriveItem
import snoop
from snoop import pp


class PdfSpider(scrapy.Spider):
    name = "pdf"
    allowed_domains = ["www.pdfdrive.com"]
    start_urls = ["https://www.pdfdrive.com/search?q=tom+hardy", "https://pdfdrive.com/search?q=tom hardy&page=2"]

    @snoop
    def parse(self, response):
        pd = PdfdriveItem()
        pd["link"] = response.xpath('//div[@class="file-right"]/a/@href').getall()
        return pd
