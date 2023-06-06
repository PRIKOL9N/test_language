import time

from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert len(button) > 0, "button is not found"
