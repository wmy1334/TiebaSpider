# -*- coding: utf-8 -*-
import re
from pprint import pprint

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class TiebaSpiderSpider(scrapy.Spider):
    name = 'tieba_spider'
    allowed_domains = ['tieba.baidu.com']
    base_url = 'http://tieba.baidu.com/'

    def start_requests(self):
        start_keywords = ['amd']
        for keyword in start_keywords:
            yield Request(
                url='http://tieba.baidu.com/mo/q---5E774EF7CC93D6A4A9A6D3345BF15460%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1542766882020_312/m?pnum=1&kw={keyword}'.format(
                    keyword=keyword),
                callback=self.parse)

    def parse(self, response):
        if 'pnum=1' in response.url:
            total_page = response.xpath('//div[@class="bc p"]/input[@type="text"]/@value').extract_first()
            if total_page:
                total_page = int(total_page)
                for page_num in range(2, total_page + 1):
                # for page_num in range(2, 3):
                    page_url = response.url.replace('pnum=1', 'pnum={}'.format(page_num))
                    yield Request(url=page_url, callback=self.parse, dont_filter=True)
        print(response.url)
        div_list = response.xpath('//div/div[contains(@class, "i")]')
        for div in div_list[:1]:
            tweet_item = {}
            tweet_item['tieba_name'] = response.xpath("//div/div[@class='bc']/text()").extract_first().split(u"\xa0")[0]
            tweet_item['url'] = response.url.split('m?')[0] + div.xpath('./a/@href').extract_first() + "&is_bakan=0"
            # tweet_item['title'] = div.xpath('./a/text()').extract_first()
            tweet_item['is_digest'] = bool('精' in ''.join(div.xpath('.//text()').extract()))

            yield Request(
                url=tweet_item['url'],
                callback=self.pares_detail,
                meta={'item': tweet_item}
            )

            yield Request(
                url=tweet_item['url'],
                callback=self.parse_comment
            )

    def pares_detail(self, response):
        tweet_item = response.meta['item']
        tweet_item['title'] = response.xpath("//div[@class='bc p']/strong/text()").extract_first()
        tweet_item["tweet_user_name"] = response.xpath(
            '//div[@class="d"]/div[@class="i" and position()=1]//table/tr/td/span[@class="g"]/a/text()').extract_first()
        tweet_item["tweet_time"] = response.xpath(
            '//div[@class="d"]/div[@class="i" and position()=1]//table/tr/td/span[@class="b"]/text()').extract_first()
        tweet_item['tweet_id'] = re.findall(r'kz=(\d*?)&', response.url)[0]
        pprint(tweet_item)
        yield tweet_item

    def parse_comment(self, response):
        comment_div_list = response.xpath("//div[@class='d']/div[@class='i']")
        for div in comment_div_list:
            comment_item = {}
            comment_item['tweet_id'] = re.findall(r'kz=(\d*?)&', response.url)[0]
            content_text = div.xpath("./text()").extract_first()
            comment_item['comment_content'] = content_text
            comment_item['comment_floor'] = content_text[:2]
            img_url_list = div.xpath('.//img/@href').extract()
            comment_item['comment_img'] = img_url_list if img_url_list else None
            comment_item['comment_user'] = div.xpath('./table/tr/td/span[@class="g"]/a/text()').extract_first()
            comment_item['comment_time'] = div.xpath('./table/tr/td/span[@class="b"]/text()').extract_first()
            pprint(comment_item)
            yield comment_item

        next_page_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_page_url:
            next_page_url = response.url.split('m?')[0] + next_page_url + "&is_bakan=0"
            yield Request(url=next_page_url, callback=self.parse_comment)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('tieba_spider')
    process.start()
