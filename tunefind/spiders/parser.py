# -*- coding: utf-8 -*-
from itertools import zip_longest

import scrapy


class ParserSpider(scrapy.spiders.SitemapSpider):
    name = 'parser'
    allowed_domains = ['tunefind.com']
    sitemap_rules = [
        ('/artist', 'parse_artist'),
    ]
    sitemap_urls = [
        'https://www.tunefind.com/sitemap.xml'
    ]

    def parse_artist(self, response):
        song_titles = response.css('[class*="AppearanceRow__songInfoTitle___"] ::text').extract()
        song_subtitles = response.css('[class*="AppearanceRow__songInfoSubtitle"] ::text').extract()
        event_descriptions = response.css('[class*="EpisodeDescription"] ::text').extract()
        event_titles = response.css('span[class*="EventLink__eventTitle__"] ::text').extract()
        event_dates = response.css('[class*="SongEventRow__EpisodeInfo"] time::text').extract()
        event_link_texts = response.css('[class*="EventLink__episodeMeta"] z').extract()
        event_links = response.css('[class*="EventLink__episodeMeta"] a::attr(href)').extract()

        data = {
            'url': response.request.url,
            'song_titles': song_titles,
            'song_sub_titles': song_subtitles,
            'events': []
        }
        for song_events in zip_longest(event_titles, event_descriptions, event_dates, event_links, event_link_texts,
                                       fillvalue=''):
            title, description, date, link, link_text = song_events
            data['events'].append({
                'title': title,
                'description': description,
                'date': date,
                'link': {
                    'text': link_text,
                    'url': link
                },
            })
        yield data
