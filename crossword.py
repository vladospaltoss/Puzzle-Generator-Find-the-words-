from selenium import webdriver
from selenium.webdriver.common.by import By
import time

download_dir = "E:\\selenium_course\\pythonToday"

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}

options = webdriver.EdgeOptions()
options.add_argument('--headless')
options.add_argument('--log-level=3')
options.add_experimental_option("prefs", profile)

driver = webdriver.Edge(options=options)

url = 'https://childdevelop.info/generator/letters/puzzle.html#preview'

try:
    lang = input('select language en/ru: ')
    print('-' * 20)
    words_input = input("Please type your words with ',' (max 15): ")
    time.sleep(5)

    driver.get(url=url)
    time.sleep(5)
    print('Open site...')

    print('Loginning...')
    # driver.find_element(By.XPATH, '//button[@title="Войти"]')
    driver.find_element(By.CLASS_NAME, 'login-bar_login-btn').click()
    time.sleep(5)
    login = driver.find_element(By.ID, 'login')
    login.clear()
    login.send_keys('vladosour@gmail.com')
    time.sleep(3)

    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('opergom2')
    time.sleep(3)

    submit = driver.find_element(By.XPATH, '//button[@for="login-form"]').click()
    time.sleep(5)
    print('Login complete...')
    

    if lang == 'ru':
        laguage = driver.find_element(By.ID, 'ru').click()
    elif lang == 'en':
        laguage = driver.find_element(By.ID, 'en').click()
    else:
        print('Please choose correct value!')
    time.sleep(5)

    direction = driver.find_element(By.ID, "input-s").click()
    students = driver.find_element(By.ID, 'puzzle-student').click()
    print('Params submited...')

    words = driver.find_element(By.ID, 'puzzle-words')
    words.clear()
    words.send_keys(words_input)
    time.sleep(5)
    print('Text sended...')

    make_button = driver.find_element(By.CLASS_NAME, 'generator-form_btn-make').click()
    time.sleep(5)

    download_button = driver.find_element(By.CLASS_NAME, 'generator-form_btn-download').click()
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    print('Switch page')
    link = driver.current_url
    link = link[:26] + link[82:108] + '.pdf'
    driver.get(link)
    time.sleep(5)
    print('Download complete...')


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

