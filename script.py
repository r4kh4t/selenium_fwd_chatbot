from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
URL="https://sit.veservecompany.com/chatbot-cms/login"
# path = './data/1_folder/'

# driver = webdriver.Chrome("C:\Python38\Lib\site-packages\selenium\webdriver\chrome/chromedriver.exe")
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

num=1

driver.get(URL)
login = driver.find_element_by_xpath(f'//*[@id="normal_login_username"]')
password = driver.find_element_by_xpath(f'//*[@id="normal_login_password"]')

login.send_keys('fung_sit')
password.send_keys('password')
password.submit()
time.sleep(5)
link_list = driver.find_elements_by_class_name('ant-menu-item')

for p in link_list:
     print(num,".",p.text)
     num=num+1

user_number = input ("What do you want to check?")
variant=int(user_number)
if(variant==1):
     page = driver.find_element_by_xpath(f'//*[@id="root"]/div/section/aside/div/div[2]/ul/li[1]/a')
     page.click()