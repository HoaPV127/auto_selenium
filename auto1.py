import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

mobile_emulation = {
    'deviceMetrics': {'width': 360, 'height': 640, 'pixelRatio': 3.0},
    'userAgent': 'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1'}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(240, 640)
driver.set_window_position(2000, 0)
driver.get('https://m.facebook.com')
# time.sleep(5)

# click signin
driver.find_element(By.ID, 'signup-button').click()
# time.sleep(5)

# fill name and click next 
driver.find_element(By.ID, 'firstname_input').send_keys('harry')
driver.find_element(By.ID, 'lastname_input').send_keys('potter')
driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[1]').click()
# time.sleep(20)

# select DoB
time.sleep(0.5)
driver.find_element(By.ID, 'day').send_keys('19')
driver.find_element(By.ID, 'month').send_keys('Dec')
driver.find_element(By.ID, 'year').send_keys('1999')
driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[1]').click()
# time.sleep(5)

# select signup by email
input()
# option_email = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/form/div[11]/div/a[1]')
# option_phone = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/form/div[11]/div/a[1]')
# driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", option_email, '')
# driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", option_phone, 'hidden_elem')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign up using email address').click()

# https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk
#mobile-reg-form > div:nth-child(28) > div > a:nth-child(1)

while True:
    pass
