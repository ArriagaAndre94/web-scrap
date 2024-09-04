from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

from itemloaders.processors import MapCompose 

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = 'ebay'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT':20
    }  

    download_dealy = 1

    # allowed_domains = ['listado.mercadolibre.com.ec','articulo.mercadolibre.com.ec']

    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=lego&_sacat=0']

    rules = (
      #paginacion
      Rule(
        LinkExtractor(
            allow=r'/_pgn'
        ), follow = True
      ),  
      #detalle productos
      Rule(
        LinkExtractor(
            #   utiliza expresiones regulares
              allow=r'/itm/'
          ), follow = True, callback="parse_items"
      )
    )

    def parse_items(self, response):
        print(response)
        # item = ItemLoader(Articulo(),response)
        # item.add_xpath('titulo','//h1[@class="x-item-title__mainTitle"]/span[1]/text()')
        # item.add_xpath('precio','//div[@class="x-price-primary"]/span/text()')
        # item.add_xpath('descripcion','//span[@class="ux-icon-text__text"]/span[@class="clipped"]/text()')

        # yield item.load_item()