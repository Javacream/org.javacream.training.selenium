from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import sys
sys.path.append('tests/python')
import driver_configuration as config

class ChallengingPage:
    def __init__(self):
        self.url = 'https://the-internet.herokuapp.com/challenging_dom'
        self.driver: config.Browser = config.local()
        self.driver.get(self.url)
    def close(self):
        self.driver.quit()

    def get_title(self):
        return self.driver.title   

    def get_blue_button(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "button")
        return [element for element in buttons if element.get_attribute["class"] == ["button"]]
    def get_table_row_four(self):
        pass
 
    def get_table_cell_one_five(self):
        pass
