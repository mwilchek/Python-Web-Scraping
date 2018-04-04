import scrapy


class QuotesSpider(scrapy.Spider):
    name = "backpage.com"

    def start_requests(self):

        urls = [
            'http://nova.backpage.com/WomenSeekMen'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # will return dictionary of URL posts and URL Post Titles
    def parse(self, response):
        for post in response.css("div.cat "):  # list div item where data is
            yield {
                'PostLink': post.css('a::attr(href)').extract_first(),
                'PostTitle': post.css('a::text').extract_first()
            }

            next_page = post.css('a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse_post_content)

    # will return content for each post
    def parse_post_content(self, response):
        for post in response.css("div.posting"):
            yield {
                'Profile_URL': post.css('a::attr(href)').extract_first(),
                'Age': post.css("p.metaInfoDisplay::text").re(r'\d+')
                #'Location': post.css()
            }
