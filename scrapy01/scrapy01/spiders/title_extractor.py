import scrapy


class TitleExtractorSpider(scrapy.Spider):
    """
    Extracting the title of the movie.
    """
    name = "title_extractor"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/title/tt1375666/"]
    custom_settings = {
        # Defining a fake User_Agent
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    def parse(self, response):
        print(response.css('h1 span::text').extract_first())
