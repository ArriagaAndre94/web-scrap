import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://www.olx.in/')
# sleep(2)
driver.refresh()
# sleep(2)

try:
    disclaimer_boton = driver.find_element(By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')
    disclaimer_boton.click()
except:
    pass

for i in range(3): # Voy a darle click en cargar mas 3 veces
    try:
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        # boton = driver.find_element(By.XPATH, '//button[@data-aut-id="btnLoadMore"]')
        # le doy click
        boton.click()
        # nAnuncios = 20 + (( i + 1 ) * 20 ) # 20 anuncios de carga inicial, y luego 20 anuncios por cada click que he dado
        nAnuncios = 20  # 20 anuncios de carga inicial, y luego 20 anuncios por cada click que he dado
        # Espero hasta 10 segundos a que toda la informacion del ultimo anuncio este cargada
        print(nAnuncios)
        # break
        WebDriverWait(driver, 15).until(
          EC.presence_of_element_located((By.XPATH, '//li[contains(@data-aut-id, "itemBox")][' + str(nAnuncios) + ']'))
        )
    except Exception as e:
        print('error')
        print(e)
        # si hay algun error, rompo el lazo. No me complico.
        break

anuncios = driver.find_elements(By.XPATH, '//li[contains(@data-aut-id, "itemBox")]')


for anuncio in anuncios:
    try:
        # Por cada anuncio hallo el precio
        precio = anuncio.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text
        print (precio)
        # Por cada anuncio hallo la descripcion
        descripcion = anuncio.find_element(By.XPATH, './/div[@data-aut-id="itemTitle"]').text
        print (descripcion)
    except Exception as e:
        print ('Anuncio carece de precio o descripcion')