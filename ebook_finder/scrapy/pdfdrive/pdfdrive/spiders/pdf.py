import scrapy
import snoop

from snoop import pp


class PdfSpider(scrapy.Spider):
    name = 'pdf'
    allowed_domains = ['www.pdfdrive.com']
    start_urls = ['https://www.pdfdrive.com/search?q=tom+waits']

    @snoop
    def parse(self, response):
        title = response.xpath('//h2/text()').getall()
        link = response.xpath('//div[@class="file-right"]/a/@href').getall()

        for item in zip(title, link):
            results = {
                'title': item[0],
                'link': item[1],
            }
            yield results