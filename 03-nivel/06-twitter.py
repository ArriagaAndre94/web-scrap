from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://twitter.com/login')

user = "arriaga109407@gmail.com"
password = "Arriaga1987"

userT = "ArriagaAndre94"
search = "Fraude CHN"


input_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@name="text"]')))
input_user.send_keys(userT)

# sleep(50)

# '//button[@class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l" and @control-id="ControlID-4"]'

next_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Next")]')))
next_button.click()

# sleep(500)

try:
    input_pass = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//input[@name="password"]')))
    input_pass.send_keys(password)
except:
    input_user = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//input[@name="text"]')))
    input_user.send_keys(user)
    
    next_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Next")]')))
    next_button.click()
    
    input_pass = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//input[@name="password"]')))
    input_pass.send_keys(password)   
    

# sleep(500)

next_button_pass = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Log in")]')))
next_button_pass.click()

# tweets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))

# for tweet in tweets:
#   print(tweet.text)


# try:
input_search = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@enterkeyhint="search"]')))
input_search.send_keys(search + Keys.RETURN)
# except e as Exception:
#     print(e)
     

tweets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))

for tweet in tweets:
  print(tweet.text)

sleep(1000)