import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://www.olx.in/cars_c84')
sleep(2)
driver.refresh()
sleep(2)

try:
    disclaimer_boton = driver.find_element(By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')
    disclaimer_boton.click()
except:
    pass

autos = driver.find_elements(By.XPATH, '//li[@data-aut-id="itemBox"]')

for auto in autos:
    try:
        # Por cada anuncio hallo el precio
        precio = auto.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text
        print (precio)
        # Por cada anuncio hallo la descripcion
        descripcion = auto.find_element(By.XPATH, './/div[@data-aut-id="itemTitle"]').text
        print (descripcion)
    except Exception as e:
        print ('Anuncio carece de precio o descripcion')