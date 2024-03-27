import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class CrawlImdbSpider(CrawlSpider):
    """
    Crawling on imdb and extracting the information of the top 250 movies.
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
            # Variables.
            movie_name = response.css('h1 span::text').extract_first()
            movie_year = response.css(
                'ul.ipc-inline-list > li.ipc-inline-list__item > a.ipc-link--baseAlt[href*="releaseinfo"]::text').get()
            movie_rating = response.css("span.sc-bde20123-1::text").get()
            movie_vote = response.css("div.sc-bde20123-3::text").get()
            movie_genre = response.xpath("//div[@class='ipc-chip-list__scroller']//a//text()").getall()
            movie_duration = response.css('ul.ipc-inline-list > li.ipc-inline-list__item:nth-child(3)::text').get()
            movie_director = response.css("a.ipc-metadata-list-item__list-content-item::text").get()
            movie_writer = set(
                response.css(
                    'ul.ipc-metadata-list li:nth-child(2).ipc-metadata-list__item > '
                    'div.ipc-metadata-list-item__content-container > ul.ipc-inline-list > li.ipc-inline-list__item > '
                    'a.ipc-metadata-list-item__list-content-item[href*="/name/nm"]::text').getall())
            movie_stars = set(response.xpath("//a[text()='Stars']/following-sibling::div//a//text()").getall())
            movie_synopsis = response.css('span.sc-466bb6c-1::text').get()
            movie_link = response.url

            # Prints.
            print("Movie name: {}".format(movie_name))
            print("Date of Release: {}".format(movie_year))
            print("IMDB Rating: {}/10 - {} Vote".format(movie_rating, movie_vote))
            print("Genre: {}".format(", ".join(str(item) for item in movie_genre)))
            print("Duration: {}".format(movie_duration))
            print("Director: {}".format(movie_director))
            print("Writer(s): {}".format(", ".join(str(item) for item in movie_writer)))
            print("Stars: {}".format(", ".join(str(item) for item in movie_stars)))
            print("Synopsis : {}".format(movie_synopsis))
            print("Link: {}".format(movie_link))


        elif theType == "genres":
            print("This title is the first movie of a genre.")
            print(response.css('a h3::text').extract_first())
            print(response.url)
