import unittest
from tests.python.base_firefox_test import BaseFirefoxTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

class TestDemo(BaseFirefoxTest):
  
  def test_title_is_Javacream(self):
    self.driver.get("http://javacream.org/")
    self.driver.set_window_size(1120, 692)
    self.assertEqual('Javacream', self.driver.title)

if __name__ == '__main__':
  unittest.main()
