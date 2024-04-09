# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from translate import Translator


class Scrapy01Pipeline:
    def process_item(self, item, spider):
        translator = Translator(to_lang='fa')
        tarjome = translator.translate(item['movie_name'])
        item['movie_name'] += ' ({})'.format(tarjome)
        return item
