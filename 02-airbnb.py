from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
opts.add_argument("--headless")
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://www.airbnb.com/')

sleep(3)

titulos_anuncios = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')

for elemento in titulos_anuncios:
    print(elemento.text)


print('fin')