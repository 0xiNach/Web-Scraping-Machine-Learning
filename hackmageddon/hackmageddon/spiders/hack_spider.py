from hackmageddon.items import HackmageddonItem
from scrapy import Spider, Request
from selenium import webdriver
from scrapy.selector import HtmlXPathSelector
import re
import time


class HackmageddonSpider(Spider):
	name = "hackmageddon"
	allowed_urls = ["http://www.hackmageddon.com/"]
	start_urls = ["http://www.hackmageddon.com/2015/07/06/16-30-jun-2015-cyber-attacks-timeline/"]
	
	# def __init__(self):

	# 	self.driver = webdriver.Chrome()



			




	def parse(self,response,i=[0]):
		
		#while True:
		
		i[0] += 1		
		

		if i[0] != 1:
			if (re.findall('^(?!.*{}).*{}.*$'.format('statistics','\d+-\d+-\w+-\d+'),response.meta['link']) == []):
				link = response.xpath('//a[@rel="next"]/@href').extract_first()
				yield Request(link, callback= self.parse,meta={'link': link})
			elif (re.findall('^(?!.*{}).*{}.*$'.format('statistics','\d+-\d+-\w+'),response.meta['link']) == []):
				link = response.xpath('//a[@rel="next"]/@href').extract_first()
				yield Request(link, callback= self.parse,meta={'link': link})

		
		rows = response.xpath('//tbody[@class="row-hover"]//tr')
		if not rows:
			rows = response.xpath('//tbody/tr')	
		print('='*30)
		print(i[0])
		print('='*30)


		for row in rows:
			year = response.xpath('//a[@rel="tag"]/text()').extract()[0]
			date = row.xpath('./td[2]/text()').extract()
			author = row.xpath('./td[3]/text()').extract()
			target = row.xpath('./td[4]/text()').extract()
			description = row.xpath('./td[5]/text()').extract()
			if not description:
				description = row.xpath('./td[5]/a/text()').extract()
			attack = row.xpath('./td[6]/text()').extract()
			target_class = row.xpath('./td[7]/text()').extract()
			attack_class = row.xpath('./td[8]/text()').extract()
			country = row.xpath('./td[9]/text()').extract()

			item = HackmageddonItem()
			item['Year'] = year
			item['dat'] = date
			item['Author'] = author
			item['Target'] = target
			item['Description'] = description
			item['Attack'] = attack
			item['Target_class'] = target_class
			item['Attack_class'] = attack_class
			item['Country'] = country
			yield item	

		if True:	
			link = response.xpath('//a[@rel="next"]/@href').extract_first()
			yield Request(link,callback=self.parse,meta={'link': link})		
					
					


		



	         
		
	
