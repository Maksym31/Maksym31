# import scrapy
#
#
# class FootballSpider(scrapy.Spider):
#     name = 'football'
#     start_urls = [
#         'https://www.premierleague.com/match/66441',
#     ]
#
#     def parse(self, response):
#         result = response.css('.score.fullTime::text').getall()
#         print(result)
#         yield {
#             'result': result
#         }
