#     # Tests that the method can successfully parse a response with valid JSON 

# class 
#     def test_valid_json_response(self):
#         response = scrapy.http.Response(url='https://www.mymarket.ge/ru/pr/1', body='{"data":{"Prs":[{"product_id":1,"title":"title1"},{"product_id":2,"title":"title2"}]}}', status=200)
#         list(self.spider.iter_tickets)[0].url = 'https://www.mymarket.ge/ru/pr/1'
#         expected_ad = AdScraperItem()
#         expected_ad['url'] = 'https://www.mymarket.ge/ru/pr/1'
#         expected_ad['title'] = 'title1'
#         expected_ad['ticket'] = list(self.spider.iter_tickets)[0]
#         self.assertEqual(list(self.spider.parse(response))[0], expected_ad)