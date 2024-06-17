"""
TEST MAIN
"""
import time

from Data import Data
from Locators import Locator

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# exceptions
from selenium.common.exceptions import *


class Testsubmit():

    # Fixtures are defined using the @pytest.fixture decorator in Python.
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.get(Data.WebData().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    @pytest.mark.html
    def test_login(self, boot):
        try:

            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, Locator.WebLocators().expandAllLocator))).click()

            # This is used to locate the name and send keys "vijay"
            self.wait.until(EC.presence_of_element_located(
                (By.NAME, Locator.WebLocators().nameLocator))).send_keys(Data.WebData().name)
            # This is used to locate the start of date of birth and send keys to the locator
            self.wait.until(EC.presence_of_element_located((By.NAME, Locator.WebLocators(
            ).dob_start_Locator))).send_keys(Data.WebData().fromBirthDate)
            # This is used to locate the end of date of birth and send keys to the locator
            self.wait.until(EC.presence_of_element_located((By.NAME, Locator.WebLocators(
            ).dob_start_Locator))).send_keys(Data.WebData().toBirthDate)

            # This is used to locate the search button and click on that
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, Locator.WebLocators().searchbtnLocator))).click()

            # After clicking on the button our output will showing on the screen it will check whether output displayed or not
            if self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.WebLocators().outputLocator))).is_displayed():
                print("Successfully searched")

        except NoSuchElementException as e:
            print(e)
