from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://sinoptik.ua/")
driver.maximize_window()

time.sleep(3)
driver.quit()