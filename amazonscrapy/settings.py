BOT_NAME = 'amazonscrapy'

SPIDER_MODULES = ['amazonscrapy.spiders']
NEWSPIDER_MODULE = 'amazonscrapy.spiders'

ROBOTSTXT_OBEY = True

RANDOM_UA_PER_PROXY = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
    'amazonscrapy.pipelines.AmazonscrapyPipeline': 300,
}
