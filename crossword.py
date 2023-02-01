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
    print('-' * 20)
    lang = input('select language en/ru: ')
    print('-' * 20)
    words_input = input("Please type your words with ',' (max 15): ")
    print('-' * 20)
    # time.sleep(5)

    print('Opening site...(1/11)')
    driver.get(url=url)
    start_time = time.time()
    # time.sleep(5)
    print('Site is open...(2/11)')

    print('Logining...(3/11)')
    driver.find_element(By.CLASS_NAME, 'login-bar_login-btn').click()
    # time.sleep(5)
    login = driver.find_element(By.ID, 'login')
    login.clear()
    login.send_keys('fxisesfxgdklxruqwv@tmmcv.com')
    # time.sleep(3)

    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('lox12345')
    # time.sleep(3)

    submit = driver.find_element(By.XPATH, '//button[@for="login-form"]').click()
    # time.sleep(5)
    print('Login complete...(4/11)')
    
    print('Submit params...(5/11)')
    if lang == 'ru':
        laguage = driver.find_element(By.ID, 'ru').click()
    elif lang == 'en':
        laguage = driver.find_element(By.ID, 'en').click()
    else:
        print('Please choose correct value!')
    # time.sleep(5)

    direction = driver.find_element(By.ID, "input-s").click()
    students = driver.find_element(By.ID, 'puzzle-student').click()
    print('Params submited...(6/11)')

    print('Sending text...(7/11)')
    words = driver.find_element(By.ID, 'puzzle-words')
    words.clear()
    words.send_keys(words_input)
    # time.sleep(1)
    print('Text sended...(8/11)')

    make_button = driver.find_element(By.CLASS_NAME, 'generator-form_btn-make').click()
    print('Crossword maked...(9/11)')
    time.sleep(2)

    download_button = driver.find_element(By.CLASS_NAME, 'generator-form_btn-download').click()
    time.sleep(2)

    print('Page switched...(10/11)')
    driver.switch_to.window(driver.window_handles[1])
    
    print('Download complete...(11/11)')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    end_time = time.time()
    print(f'Programm finished in {end_time - start_time} seconds')


