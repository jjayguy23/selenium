from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
 
service = Service(executable_path='./chromedriver')
chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_button2 = chrome_browser.find_element(By.CSS_SELECTOR,'#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('LOOK WHAT I CAN DO')

time.sleep(2)
show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'LOOK WHAT I CAN DO' in output_message.text

while True:
    pass
