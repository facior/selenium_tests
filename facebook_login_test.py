from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

website = 'https://facebook.com'
path = '/Users/facior/Desktop/TESTY NAUKA/chromedriver'

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get(website)
driver.maximize_window()
time.sleep(3)

accept = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]")
accept.click()

time.sleep(2)

username = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
username.send_keys("Tested@byLukaszKubieniec.com")

time.sleep(2)

password = driver.find_element(By.NAME, "pass")
password.send_keys("P4sSw0rD")

time.sleep(2)

login = driver.find_element(By.NAME, "login")
login.click()

#driver.quit()