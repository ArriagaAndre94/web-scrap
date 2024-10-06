from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Definimos el User Agent en Selenium utilizando la clase Options
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
# Agregar a todos sus scripts de selenium para que no aparezca la ventana de seleccionar navegador por defecto: (desde agosto 2024)
opts.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

#URL SEMILLA (cambio septiembere 2024)
driver.get('https://listado.mercadolibre.com.ec/arrancador-de-baterias')

PAGINACION_MAX = 10
PAGINACION_ACTUAL = 1

try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
  disclaimer = driver.find_element(By.XPATH, '//button[@data-testid="action:understood-button"]')
  disclaimer.click() # lo obtenemos y le damos click
except Exception as e:
  print (e) 
  None

# Mientras la pagina en la que me encuentre, sea menor que la maxima pagina que voy a sacar... sigo ejecutando...
while PAGINACION_MAX > PAGINACION_ACTUAL:
    links_productos = driver.find_elements(By.XPATH, '//h2[@class="poly-box poly-component__title"]/a')
    links_de_la_pagina = []
    for a_link in links_productos:
        links_de_la_pagina.append(a_link.get_attribute("href"))

    for link in links_de_la_pagina:
        sleep(2) # Prevenir baneos de IP
        try:
            # Voy a cada uno de los links de los detalles de los productos
            driver.get(link)
            titulo = driver.find_element(By.XPATH, '//h1').text
            precio = driver.find_element(By.XPATH, '//span[contains(@class,"ui-pdp-price")]').text
            print (titulo)
            print (precio.replace('\n', '').replace('\t', '')) # Podriamos realizar mas limpieza
            driver.back()
        except Exception as e:
            print (e)
            # Si sucede algun error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
            driver.back()

    try:
    # Intento obtener el boton de SIGUIENTE y le intento dar click
        puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        puedo_seguir_horizontal.click()
    except: 
    # Si obtengo un error al intentar darle click al boton, quiere decir que no existe
    # Lo cual me indica que ya no puedo seguir paginando, por ende rompo el While
        break

    PAGINACION_ACTUAL += 1