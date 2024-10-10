from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys

def obtener_script_scrolling(iteration): 
    scrollingScript = """ 
      window.scrollTo(0, 20000)
    """
    return scrollingScript.replace('20000', str(20000 * (iteration + 1)))

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://www.youtube.com/playlist?list=PLuaGRMrO-j-8NndtkHMA7Y_7798tdJWKH')

videos = driver.find_elements(By.XPATH, '//div[@id="contents"]/ytd-playlist-video-renderer')

url_videos = []

for video in videos:
    url = video.find_element(By.XPATH, './/h3/a[@id="video-title"]').get_attribute("href")
    url_videos.append(url)

print(url_videos)

for url in url_videos:
    driver.get(url)
    sleep(3)
    
    driver.execute_script("""window.scrollTo(0, 400)""")
    sleep(3)
    
    num_comentarios_totales = driver.find_element(By.XPATH, '//h2[@id="count"]//span[1]').text
    num_comentarios_totales = int(num_comentarios_totales) * 0.90
    
    print('Comentarios totales:', num_comentarios_totales)
    
    comentarios_cargados = len(driver.find_elements(By.XPATH, '//div[@id="body"]'))
    
    n_scrolls = 0
    n_scrolls_maximo = 10
    while comentarios_cargados < num_comentarios_totales and n_scrolls < n_scrolls_maximo:
        driver.execute_script(obtener_script_scrolling(n_scrolls))
        n_scrolls += 1
        sleep(2)    
        comentarios_cargados = len(driver.find_elements(By.XPATH, '//div[@id="body"]'))
        print('Comentarios cargados', comentarios_cargados)
        
        
    
    comentarios = driver.find_elements(By.XPATH,'//yt-attributed-string[@id="content-text"]')
    for comentario in comentarios:
        texto_comentario = comentario.text
        print(texto_comentario+ '\n\n')

    


sleep(500)