import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://dicabienlinea.minfin.gob.gt/dicabi_enlinea/consultaedomat.aspx')
sleep(2)
driver.refresh()
sleep(2)

try:
    filtro = driver.find_element(By.XPATH, '//select[@name="ctl00$ContentPlaceHolder1$ddlFiltro"]')
    # filtro.send_keys('Nit igual a')
    filtroSelect = Select(filtro)
    filtroSelect.select_by_visible_text('Nit igual a')
    # filtro.select_by_value('Nit igual a')
    textbox = driver.find_element(By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$txtDatoBuscar"]')
    textbox.clear()
    # textbox.send_keys('1796688380301')
    textbox.send_keys('90494-5')
    # textbox.send_keys('1729918540101')
    disclaimer_boton = driver.find_element(By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$btnVerEstado"]')
    disclaimer_boton.click()

    driver.save_screenshot('/Users/andre/Desktop/screenshot.png')
    
except Exception as e:
        print(e)

import pytesseract
from PIL import Image

# Especifica la ruta de la imagen que deseas analizar
image_path = "/Users/andre/Desktop/screenshot.png"

# Cargar la imagen con Pillow
img = Image.open(image_path)

# Realiza OCR en la imagen
text = pytesseract.image_to_string(img)

# Imprime el texto extraído
print(text)

# Opcional: Guarda el texto extraído en un archivo
with open("/Users/andre/workspace/web-scrap/03-nivel/output_text.txt", "w") as f:
    f.write(text)


# autos = driver.find_elements(By.XPATH, '//li[@data-aut-id="itemBox"]')

# for auto in autos:
#     try:
#         # Por cada anuncio hallo el precio
#         precio = auto.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text
#         print (precio)
#         # Por cada anuncio hallo la descripcion
#         descripcion = auto.find_element(By.XPATH, './/div[@data-aut-id="itemTitle"]').text
#         print (descripcion)
#     except Exception as e:
#         print ('Anuncio carece de precio o descripcion')


driver.close()
