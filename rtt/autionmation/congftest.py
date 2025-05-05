

import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service

@pytest.fixture()
def setup():
    ser_obj = Service("/usr/bin/chromedriver")
    driver =webdriver.Chrome(service=ser_obj)
    driver.maximize_window()

    return driver