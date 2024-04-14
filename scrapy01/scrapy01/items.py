# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy01Item(scrapy.Item):
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()
    movie_rating = scrapy.Field()
    movie_vote = scrapy.Field()
    movie_genre = scrapy.Field()
    movie_duration = scrapy.Field()
    movie_director = scrapy.Field()
    movie_writer = scrapy.Field()
    movie_stars = scrapy.Field()
    movie_synopsis = scrapy.Field()
    movie_link = scrapy.Field()
