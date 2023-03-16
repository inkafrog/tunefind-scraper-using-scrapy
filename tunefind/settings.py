# -*- coding: utf-8 -*-
BOT_NAME = 'tunefind'

SPIDER_MODULES = ['tunefind.spiders']
NEWSPIDER_MODULE = 'tunefind.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS = 6

DUPEFILTER_CLASS = 'tunefind.filters.avoid_parsed_urls.Filter'
JSON_FILE_NAME = "response.jl"

# retry if there is error
RETRY_TIMES = 20
# Retry for 403
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403]

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# UA settings
RANDOM_UA_ENABLED = True
RANDOM_UA_DEFAULT_TYPE = 'desktop'
# always change user-agent
RANDOM_UA_OVERWRITE = False

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}


DB_SETTINGS = {
    'db': 'new_tunefind',
    'user': 'root',
    'password': '#takeOver123',
    'host': '127.0.0.1',
    'port': 3306,
}
