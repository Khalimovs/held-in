import scrapy

class ChallengeSpider(scrapy.Spider):

    name = 'challenge'

    start_urls = [
        'https://kun.uz/',
        'https://daryo.uz/'
    ]

    def parse(self, response):
        page = response.url.split('/')[-2]
        file_name = f'res_{page}.html'
        with open(file_name, 'wb') as f:
            f.write(response.body)