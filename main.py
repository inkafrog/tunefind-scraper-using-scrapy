from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from tunefind.spiders.parser import ParserSpider

if __name__ == '__main__':
    settings = get_project_settings()
    settings.setdict({
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': settings.get('JSON_FILE_NAME')
    })

    process = CrawlerProcess(settings=settings)
    process.crawl(ParserSpider)
    process.start()
