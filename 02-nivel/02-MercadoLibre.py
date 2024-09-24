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
    name = 'mercadoLibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT':20
    }  

    download_dealy = 1

    allowed_domains = ['listado.mercadolibre.com.ec','articulo.mercadolibre.com.ec']

    start_urls = ['https://listado.mercadolibre.com.ec/animales-mascotas/perros/']

    rules = (
      #paginacion
      Rule(
        LinkExtractor(
            allow=r'/_Desde_'
        ), follow = True
      ),  
      #detalle productos
      Rule(
        LinkExtractor(
            #   utiliza expresiones regulares
              allow=r'/MEC-'
          ), follow = True, callback="parse_items"
      )
    )

    def parse_items(self, response):
        item = ItemLoader(Articulo(),response)
        item.add_xpath('titulo','')
        item.add_xpath('precio','')
        item.add_xpath('descripcion','')