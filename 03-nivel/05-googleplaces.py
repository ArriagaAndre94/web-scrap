import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
# Agregar a todos sus scripts de selenium para que no aparezca la ventana de seleccionar navegador por defecto: (desde agosto 2024)
opts.add_argument("--disable-search-engine-choice-screen")

def getScrollingScript(iteration): 
    # Script de scrolling es un script de javascript. Le hago scroll a un contenedor que contenta ciertas clases
    # Estas clases dependen de mi extraccion. Existen otras maneras de hacer scrolling que veremos en el NIVEL EXTRA.
    scrollingScript = """ 
      document.getElementsByClassName('m6QErb DxyBCb kA9KIf dS8AEf XiKgde ')[0].scroll(0, 20000)
    """

    # 'm6QErb DxyBCb kA9KIf dS8AEf XiKgde '

    return scrollingScript.replace('20000', str(20000 * (iteration + 1)))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
driver.get('https://www.google.com/maps/place/Restaurante+Amazonico/@40.423706,-3.6872655,17z/data=!4m7!3m6!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.423706!4d-3.6850768!9m1!1b1')

sleep(random.uniform(1.0, 2.0))

# Debemos darle click al boton de disclaimer de cookies que no interrumpa nuestras acciones
# try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
#   disclaimer = driver.find_element(By.XPATH, '//span[text()="Accept all"]')
#   disclaimer.click() # lo obtenemos y le damos click
# except Exception as e:
#   print (e) 
#   None

sleep(random.uniform(1.0, 2.0))

SCROLLS = 0
while (SCROLLS != 2): # Decido que voy a hacer 3 scrollings
  driver.execute_script(getScrollingScript(SCROLLS)) # Ejecuto el script para hacer scrolling del contenedor
  sleep(random.uniform(1, 2)) # Entre cada scrolling espero un tiempo
  SCROLLS += 1

#   //div[@class='jftiEf fontBodyMedium ']

restaurantsReviews = driver.find_elements(By.XPATH, "//div[@class='jftiEf fontBodyMedium ']")

for review in restaurantsReviews:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'WNx')]//button")) 
    )

    userLink = review.find_element(By.XPATH, ".//div[contains(@class, 'WNx')]//button")
    print(userLink)

    try:
        userLink.click() # Damos click en el nombre de display del usuario para abrir su perfil. Esto se abre en un nuevo tab.
        sleep(2) # septiembere 2024: tenemos que anadir una espera
        # Movemos el contexto del driver al tab en la segunda posicion. Si no hacemos esto, no podremos acceder a los elementos del nuevo tab.
        driver.switch_to.window(driver.window_handles[1])

        # jftiEf fontBodyMedium t2Acle FwTFEc azD0p

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='jftiEf fontBodyMedium t2Acle FwTFEc azD0p']")) # Existe el atributo data-review-id Y no existe el atributo aria-label
        )

        USER_SCROLLS = 0
        # Similar a la logica utilizada para hacer scrolling de las opiniones de un restaurante

        while (USER_SCROLLS != 2):
            driver.execute_script(getScrollingScript(USER_SCROLLS))
            sleep(random.uniform(4, 5))
            USER_SCROLLS += 1

            sleep(10)

            intReviewsWait = (USER_SCROLLS ) * 10  # 20 anuncios de carga inicial, y luego 20 anuncios por cada click que he dado
            # nAnuncios = 20  # 20 anuncios de carga inicial, y luego 20 anuncios por cada click que he dado
            # Espero hasta 10 segundos a que toda la informacion del ultimo anuncio este cargada
            print(intReviewsWait)
            # break
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='jftiEf fontBodyMedium t2Acle FwTFEc azD0p'][" + str(intReviewsWait) + "]"))
            )

            userReviews = driver.find_elements(By.XPATH,"//div[@class='jftiEf fontBodyMedium t2Acle FwTFEc azD0p']")

            for userReview in userReviews:
                reviewRating = userReview.find_element(By.XPATH, './/span[@class="kvMYJc"]').get_attribute('aria-label')
                userParsedRating = float(''.join(filter(str.isdigit or str.isspace, reviewRating))) # Codigo para solamente quedarme con los digitos de una cadena. En la clase nos quedamos con toda la cadena.
                reviewText = ""
                try:
                    reviewText = userReview.find_element(By.XPATH, './/span[@class="wiI7pd"]').text
                except:
                    print('Review sin texto')

                print(userParsedRating)
                print(reviewText)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # break


    except Exception as e:
        print(e)
        driver.close() 
        driver.switch_to.window(driver.window_handles[0])