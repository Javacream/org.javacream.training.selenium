from base_firefox_test import BaseFirefoxTest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
class DuckduckgoTest(BaseFirefoxTest):
  
  def test_title_is_DuckDuckGo(self):
    self.driver.get('https://duckduckgo.com/')
    self.assertIn('DuckDuckGo', self.driver.title)
    search_input = self.driver.find_element(by=By.ID, value="searchbox_input")
    search_button = self.driver.find_element(by=By.XPATH, value="//*[@id='searchbox_homepage']//*[@type='submit']")
    search_input.send_keys("Javacream")
    search_button.click()
    self.driver.save_screenshot("results/results.png")

if __name__ == '__main__':
  unittest.main()
