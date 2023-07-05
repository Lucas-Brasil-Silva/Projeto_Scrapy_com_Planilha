import scrapy

class ProxyScrapySpider(scrapy.Spider):
    name = 'proxybot'
    urls = ['https://free-proxy-list.net/web-proxy.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                'Proxy name': linha.xpath('./td[1]/a/text()').get(),
                'domain': linha.xpath('./td[2]/text()').get(),
                'country': linha.xpath('./td[3]/text()').get(),
                'speed': linha.xpath('./td[4]/text()').get(),
                'popularity': linha.xpath('./td/div/div/text()').get()
            }