
import unittest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from search_page import SearchPage
class TestDemo(unittest.TestCase):
  def setUp(self):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Linux need geckodriver path 
    #geckodriver_path = "/snap/bin/geckodriver"
    # driver_service = webdriver.FirefoxService(options=options, executable_path=geckodriver_path)

    # Windows
    driver_service = webdriver.FirefoxService(options=options)

    self.driver = webdriver.Firefox(service=driver_service)
    self.wait = WebDriverWait(self.driver, 10)
    self.vars = {}
    self.page = SearchPage(self.driver, self.wait)
    self.page.go_to_search_page()
    self.driver.set_window_size(1120, 692)
  
  def tearDown(self):
    self.driver.quit()
  
  def test_title_is_DuckDuckGo(self):
    self.assertIn('DuckDuckGo', self.page.get_title())

  def test_navigate_to_search(self):
    self.page.go_to_search_page()
    self.assertIn('DuckDuckGo', self.page.get_title())

  def test_make_search(self):
    self.page.make_a_search("Javacream")

if __name__ == '__main__':
  unittest.main()
