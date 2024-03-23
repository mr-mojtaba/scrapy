from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class TopMoviesSpider(CrawlSpider):
    """
    Crawling on the imdb.com and showing the title and link of the top 250 movies.
    """

    name = "top_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://imdb.com/chart/top/"]

    custom_settings = {
        # Defining a fake User_Agent
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    rules = [
        Rule(
            LinkExtractor(allow=('title/tt')),
            callback='parse_items',
            follow=False,
        ),
    ]

    i = 0

    def parse_items(self, response):
        self.i += 1
        print("\t")
        print("*" * 20)
        print(self.i)
        print("Movie name: ", response.css('h1 span::text').extract_first())
        print("Link: ", response.url)
        print("*" * 20)
        print("\t")
