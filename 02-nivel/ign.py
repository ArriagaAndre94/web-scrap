from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.selector import Selector

class Articulo(Item):
    titulo = Field()
    contenido = Field()

class Review(Item):
    titulo = Field()
    calificacion = Field()

class Video(Item):
    titulo = Field()
    fecha_de_publicacion = Field()

class IGNCrawler(CrawlSpider):
    name = 'ign'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'CLOSESPIDER_PAGECOUNT': 100
    }

    allowed_domains = ['latam.ign.com']
    download_delay = 1
    start_urls = ['https://latam.ign.com/se/?model=article&q=ps5']

    rules = (
        # Horizontalidad por tipo de información
        Rule(
            LinkExtractor(
                allow=r'type='
            ), follow=True), # HORIZONTALIDAD POR TIPO => No tiene callback ya que aqui no voy a extraer datos
        Rule(LinkExtractor(
            allow=r'&page=\d+'
            ), follow=True),
        # Una regla por cada tipo de contenido donde ire verticalemente
        #REVIEW
        Rule(
            LinkExtractor( # VERTICALIDAD DE REVIEWS
                allow=r'/review/',
                deny=r'utm_source=recirc', # Parametro deny para evitar URLs repetidas que en este caso especial de IGN son por los parametros (https://www.udemy.com/instructor/communication/qa/15832180/detail?course=2861742)
            ), follow=True, callback='parse_review'),
        Rule(
            LinkExtractor( # VERTICALIDAD DE VIDEOS
                allow=r'/video/',
                deny=r'utm_source=recirc',
            ), follow=True, callback='parse_videos'),
        Rule(
            LinkExtractor(
                allow=r'/news/', # VERTICALIDAD DE ARTICULOS
                deny=r'utm_source=recirc',
            ), follow=True, callback='parse_news'),
    )

    # DEFINICION DE CADA FUNCION PARSEADORA DE CADA TIPO DE INFORMACION

    # REVIEW
    def parse_review(self, response):
        sel = Selector(response)
        item = ItemLoader(Review(), sel)

        item.add_xpath('titulo', '//div[@class="article-headline"]/h1/text()')
        item.add_xpath('calificacion', '//span[@class="side-wrapper side-wrapper hexagon-content"]/div/text()')

        yield item.load_item()

    # VIDEO
    def parse_videos(self, response):
        sel = Selector(response)
        item = ItemLoader(Video(), sel)

        item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()')

        yield item.load_item()

    # ARTICULO
    def parse_news(self, response):
        sel = Selector(response)
        item = ItemLoader(Articulo(), sel)

        item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
        item.add_xpath('contenido', '//div[@id="id_text"]//*/text()')
        # item.add_xpath('contenido', '//div[@id="article-body"]/p/text()')

        yield item.load_item()    