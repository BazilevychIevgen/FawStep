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
# wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '10 днів')]"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Налаштування')]"))).click()


def highlight_element(driver, element, duration=2, color="red", border=2):
    original_style = element.get_attribute('style')
    highlight_style = f"border: {border}px solid {color}; background-color: rgba(255,0,0,0.1);"

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, highlight_style)
    time.sleep(duration)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style or "")


elements = driver.find_elements(By.XPATH, "//a[contains(text(), '10 днів')]")
for e in elements:
    highlight_element(driver, e, duration=1, color="lime")
    print(f"Found: {e.text}")

elements = driver.find_elements(By.XPATH, "//button[contains(text(), 'Налаштування')]")
for e in elements:
    highlight_element(driver, e, duration=1, color="lime")
    print(f"Found: {e.text}")

# Додатковий час для перегляду результату
time.sleep(3)

# Закриваємо браузер (опціонально)
driver.quit()