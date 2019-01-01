import scrapy 
from crawler.items import CrawlerItem
import re

class crawler(scrapy.spider)
	name = "myCrawler"
	
	start_url = ["https://apolloclinics.in/all-packages/"]

	def parse(self,response):
		for href in response.xpath response.xpath("//div[contains(@class, 'content')]//a[contains(@class, 'woocommerce-LoopProduct-link woocommerce-loop-product__link')]//@href")
		url  = "https:" + href.extract()
		yield scrapy.Request(url, callback=self.parse_dir_contents)


	def parse_dir_contents(self, response):
		item = CrawlerItem()


		item['producttitle'] = ''.join( response.xpath("//div[contains(@class, 'summary entry-summary')]/h1[contains(@class, 'product_title entry-title')]/text()").extract()).strip()
		
		item['servicesprovided'] = response.xpath("//td[contains(@class, 'res')]/ul/li/text()").extract()
		
		item['cities'] = response.xpath("//select[contains(@class, 'name_field form-control form-select required ajax-processed sply-question-info location')]/option[position()>1]/text()").extract()
		
		item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()
	
		yield item
