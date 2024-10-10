import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys

def getScrollingScript(iteration): 
    # Script de scrolling es un script de javascript. Le hago scroll a un contenedor que contenta ciertas clases
    # Estas clases dependen de mi extraccion. Existen otras maneras de hacer scrolling que veremos en el NIVEL EXTRA.
    scrollingScript = """ 
      document.getElementsByClassName('x6s0dn4 x78zum5 xdt5ytf x193iq5w ')[0].scroll(0, 20000)
    """

    # 'm6QErb DxyBCb kA9KIf dS8AEf XiKgde '

    return scrollingScript.replace('20000', str(20000 * (iteration + 1)))

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/CirculoDeAmigosBanrural/photos")

driver.execute_script("document.querySelector('div.__fb-light-mode.x1n2onr6.xzkaem6').remove()")

images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1lliihq x5yr21d x1n2onr6 xh8yej3"]')))
    
for image in images:
    image.click()
    sleep(2)
    driver.execute_script("""
    var event = new KeyboardEvent('keydown', {
        key: 'ArrowLeft',
        keyCode: 37,
        code: 'ArrowLeft',
        which: 37,
        bubbles: true
    });
    document.dispatchEvent(event);
""")
    sleep(500)
    print(image.get_attribute('href'))


sleep(50)