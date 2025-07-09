# -- coding: utf-8 --
from __future__ import unicode_literals
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


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"
__description__ = "Selectors for sinoptic.ua"


sinoptic = {"https://sinoptik.ua/": {"settings": "//button[contains(text(), 'Налаштування')]",
                                     "week": "//a[contains(text(), 'Тиждень')]",
                                     "10 days": "//a[contains(text(), '10 днів')]",
                                     },
            "https://sinoptik.ua/pohoda/kyiv": {"home page": "//a[contains(text(), 'Домашня сторінка')]",
                                                "settings": "//button[contains(text(), 'Налаштування')]",
                                                "week": "//a[contains(text(), 'Тиждень')]",
                                                "10 days": "//a[contains(text(), '10 днів')]",
                                                "": "",
                                                },
            }


class Sinoptik:
    def __init__(self):
        # Ініціалізація драйвера
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 10)

        # Відкриваємо сайт
        self.driver.get("https://sinoptik.ua/")

    def settings(self, text='Налаштування'):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), {text})]"))).click()
