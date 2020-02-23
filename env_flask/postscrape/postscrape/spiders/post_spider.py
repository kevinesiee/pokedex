import scrapy 
from scrapy import Request 

class PostsSpider(scrapy.Spider):
	name = "pokedex"
	allowed_domains = ['www.pokepedia.fr']
	#le site que nous allons scrapper
	start_urls = [
		'https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_dans_l%27ordre_du_Pok%C3%A9dex_National'
	]

	#un parser pour les pages 
	def parse(self, response):
		"""
			Ici nous allons prendre entièrement les deux pages HTML 
			dans deux fichiers distincts
		"""
		title = response.css('title::text').extract_first()
        all_links = {name:response.urljoin(url) for name, url in zip(response.css("#nav-markup .Nav__item")[3].css("a::text").extract(),response.css("#nav-markup .Nav__item")[3].css("a::attr(href)").extract())}
        yield {
            "title":title,
            "all_links":all_links
        }


