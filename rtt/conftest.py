

import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service


@pytest.fixture()
def setup():
    ser_obj = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=ser_obj)

    return driver