import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class CrawlimdbSpider(CrawlSpider):
    name = "crawlimdb"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]
    rules = [
        Rule(LinkExtractor(allow=('title/tt')), callback='parse_items', follow=False),
        Rule(LinkExtractor(allow=('genres')), callback='parse_genres', follow=False),
    ]

    def parse_items(self, response):
        print("This title is for the top 250 movies page.")
        print(response.url)
        print(response.css('h3::text').extract_first())

    def parse_genres(self, response):
        print("This title is the first movie of a genre.")
        print(response.url)
        print(response.css('a h3::text').extract_first())
