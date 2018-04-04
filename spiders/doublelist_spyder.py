import scrapy
import webbrowser
import time


class QuotesSpider(scrapy.Spider):
    name = "doublelist.com"

    def start_requests(self):

        urls = [
            'https://doublelist.com/age_verify/?age=over18&camefrom=/view/washington_dc/cw4m/'
        ]

        for url in urls:
            webbrowser.open(url, new=2)
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)

    # will return dictionary of items for callbacks of css tags defined and drill down to further sites linked in a post
    def parse(self, response):
        for post in response.css('div.ad-list-box'):  # list div item where data is
            yield {
                'URL': post.css('a::attr(href)::text').extract_first(),
                'Title': post.xpath('//a//text()').extract_first(),
            }

        # next_page = response.css('div.ad-list-box a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    # prints dictionary of items for callbacks of css tags defined
    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract(),
    #         }

    # saves urls defined as local html files
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
