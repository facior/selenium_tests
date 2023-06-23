from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import org.openqa.selenium.Keys

website = 'https://twitter.com/'
path = '/Users/facior/Desktop/TESTY NAUKA/chromedriver'

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get(website)
driver.maximize_window()
time.sleep(3)

time_to_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a")
time_to_login.click()

time.sleep(2)

username = driver.find_element(By.NAME, "text")
username.send_keys("facior_")

time.sleep(3)

next = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
next.click()

time.sleep(2)

password = driver.find_element(By.NAME, "password")
password.send_keys("testowe_haslo")

login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
login.click()

input_news = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
input_news.send_keys("news")
WebElement.sendKeys(Keys.ENTER)

#driver.quit()


