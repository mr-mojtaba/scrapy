import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class CrawlImdbSpider(CrawlSpider):
    """
    Crawling on imdb and extracting the title and link of the top 250 movies.
    """

    name = "crawlimdb"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    custom_settings = {
        # Defining a fake User_Agent
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    rules = [
        Rule(
            LinkExtractor(
                allow=('title/tt'),
                deny=('title/tt00'),
            ),
            callback='parse_items',
            follow=False,
            cb_kwargs={"theType": "250films"},
        ),
        Rule(
            LinkExtractor(allow=('genres')),
            callback='parse_items',
            follow=False,
            cb_kwargs={"theType": "genres"},
        ),
    ]

    def parse_items(self, response, theType):
        if theType == "250films":
            name_item = response.css('h1 span::text').extract_first()
            year_item = response.css(
                'ul.ipc-inline-list > li.ipc-inline-list__item > a.ipc-link--baseAlt[href*="releaseinfo"]::text').get()
            rating_item = response.css("span.sc-bde20123-1::text").get()
            vote = response.css("div.sc-bde20123-3::text").get()
            genre_item = response.xpath("//div[@class='ipc-chip-list__scroller']//a//text()").getall()
            duration_item = response.css('ul.ipc-inline-list > li.ipc-inline-list__item:nth-child(3)::text').get()
            director_item = response.css("a.ipc-metadata-list-item__list-content-item::text").get()
            writer_item = set(
                response.css(
                    'ul.ipc-metadata-list li:nth-child(2).ipc-metadata-list__item > '
                    'div.ipc-metadata-list-item__content-container > ul.ipc-inline-list > li.ipc-inline-list__item > '
                    'a.ipc-metadata-list-item__list-content-item[href*="/name/nm"]::text').getall())
            stars_item = set(response.xpath("//a[text()='Stars']/following-sibling::div//a//text()").getall())
            synopsis = response.css('span.sc-466bb6c-1::text').get()
            link_item = response.url

            print("Movie name: {}".format(name_item))
            print("Date of Release: {}".format(year_item))
            print("IMDB Rating: {}/10 - {} Vote".format(rating_item, vote))
            print("Genre: {}".format(", ".join(str(item) for item in genre_item)))
            print("Duration: {}".format(duration_item))
            print("Director: {}".format(director_item))
            print("Writers: {}".format(", ".join(str(item) for item in writer_item)))
            print("Stars: {}".format(", ".join(str(item) for item in stars_item)))
            print("Synopsis : {}".format(synopsis))
            print("Link: {}".format(link_item))

        elif theType == "genres":
            print("This title is the first movie of a genre.")
            print(response.css('a h3::text').extract_first())
            print(response.url)
