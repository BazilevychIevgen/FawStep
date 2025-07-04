from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ініціалізація драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Відкриваємо сайт
driver.get("https://sinoptik.ua/")

# Чекаємо поки кнопка '10 днів' стане клікабельною і клікаємо
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '10 днів')]"))).click()

# Додатковий час для перегляду результату
time.sleep(3)

# Закриваємо браузер (опціонально)
driver.quit()