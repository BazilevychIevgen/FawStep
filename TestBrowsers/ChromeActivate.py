from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://sinoptik.ua/")
driver.maximize_window()
# page_source = driver.page_source
page_source = driver.execute_script("return document.documentElement.outerHTML;")
print(page_source)


time.sleep(3)
