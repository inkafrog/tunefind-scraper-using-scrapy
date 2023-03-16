from os.path import exists

import json_lines
from scrapy.dupefilters import BaseDupeFilter

from tunefind.settings import JSON_FILE_NAME


class Filter(BaseDupeFilter):
    urls: iter

    def get_urls(self):
        if not exists(JSON_FILE_NAME):
            return []
        with json_lines.open(JSON_FILE_NAME) as fp:
            return [k['url'] for k in fp]

    def open(self):
        self.urls = tuple(self.get_urls())

    def request_seen(self, request):
        return request.url in self.urls
