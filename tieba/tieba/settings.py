# -*- coding: utf-8 -*-

# Scrapy settings for tieba project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tieba'

SPIDER_MODULES = ['tieba.spiders']
NEWSPIDER_MODULE = 'tieba.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tieba (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'USER_RS=908565156_20_30_1; BAIDUID=5E774EF7CC93D6A4A9A6D3345BF15460:FG=1; BIDUPSID=5E774EF7CC93D6A4A9A6D3345BF15460; PSTM=1541681010; __cfduid=d49c7ac4b64ab2e1e1e3a98f5bb940ae01541683164; TIEBA_USERTYPE=42145ea68a817aed34f82726; bdshare_firstime=1541829804967; TIEBAUID=bf946c1beb9c0e202df66226; BDUSS=V1VG14MjFWd1c1UWhYVjJWZHFpblBlM0I4ZVl6bDNPVkU3cnB0UWJsSWtUaHBjQVFBQUFBJCQAAAAAAAAAAAEAAACkmic2zt7BxLW9y8C1xNPjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACTB8lskwfJbdH; STOKEN=7db4f7c128f6c7e6139481a5c13768b8ab52df23b53805f9118deb3f9eff51b2; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; IS_NEW_USER=7c2a315862e2908ac9f7d3d2; USER_JUMP=-1; H_WISE_SIDS=126008_126894_126713_114552_127276_125151_126980_120161_123019_118896_118862_118855_118822_118803_127182_107317_126996_126866_125544_126142_126796_126558_117334_126792_117432_126782_126440_127027_126380_124953_126197_126773_126850_126720_126091_127048_123901_125853_127197_126398_124030_126439_110085_123290_126505_127224; FEED_SIDS=535759_1121_10; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; SE_LAUNCH=5%3A25712779_0%3A25712779; BDPASSGATE=IlPT2AEptyoA_yiU4V493kIN8enjUvWA1evESFplQFePdCyWmhHoAb-IXjLOUZm8AiTMdI3JlMldjijsQmFuirMen_cohjwdckaScNWlxBD4HxEMecIVPNDpIEE0wA0HkPNjwOEd0f6NKTsFfQC6puo4ivKl7AhN8vXFsivVhtXu2oSPYFrGzIWEPW67O-0APNuK-R0QbSh-OkOWVOGxRILYhFchOJ1L70aOatc6EO0PuT1AEeXjL4AaZGH-ACpjFQemBfmDxK; mo_originid=1; BDRCVFR[JTSKpTiD9LD]=9xWipS8B-FspA7EnHc1QhPEUf; Hm_lvt_7d6994d7e4201dd18472dd1ef27e6217=1542766759,1542766787,1542766842,1542766869; BAIDU_WISE_UID=wapp_1542766882020_312; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1542636977,1542766719,1542766861,1542766887; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1542766887; CLIENTWIDTH=411; CLIENTHEIGHT=823; LASW=411; Hm_lpvt_7d6994d7e4201dd18472dd1ef27e6217=1542766895; WIFI_SF=1542767006; SEENKW=amd%23%E6%9C%9F%E5%BE%85%E5%9C%A8%E5%9C%B0%E4%B8%8B%E5%9F%8E%E9%82%82%E9%80%85%E6%9C%89%E9%94%99%E5%90%97%23%E9%A6%96%E9%A1%B5%23%E5%88%80%E5%89%91%E7%A5%9E%E5%9F%9F%23%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2%23%E6%AD%A6%E6%B1%89; PSINO=1; H_PS_PSSID=1447_21093_27508',
'Host': 'tieba.baidu.com',
# 'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tieba.middlewares.TiebaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tieba.middlewares.TiebaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tieba.pipelines.TiebaPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
