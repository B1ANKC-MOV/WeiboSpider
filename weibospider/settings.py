# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':'SUB=_2A25yojBRDeRhGeFL6VIU9S7LyziIHXVubVAZrDV6PUJbkdANLUGjkW1NQk1ZoSAssGE6Gu3F662TO6k6_LZTsrfh; SCF=AikP-_NZNAwxlrHyc8ynvgkjGU9It3J8ReNqUXXoG010HdEnsYJMdq9UuZhUiqhmLOsj4hvYmrYeo1jYn8Y4QFE.; _T_WM=4441d33905a69d579115c5de9cec263f'
}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017