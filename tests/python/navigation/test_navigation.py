import unittest
import sys
sys.path.append('tests/python')
from base_firefox_test import BaseFirefoxTest
from selenium.webdriver.common.by import By

class Test(BaseFirefoxTest):
    def test_open(self):

        self.driver.get("https://www.selenium.dev")

        title = self.driver.title
        self.assertEqual("Selenium", title)

        url = self.driver.current_url
        self.assertEqual("https://www.selenium.dev/", url)
    def test_back_button(self):
        self.driver.get("https://www.selenium.dev")
        self.driver.get("https://www.selenium.dev/selenium/web/index.html")

        title = self.driver.title
        assert title == "Index of Available Pages"

        self.driver.back()
        title = self.driver.title
        self.assertEqual("Selenium", title)

        self.driver.forward()
        title = self.driver.title
        self.assertEqual("Index of Available Pages", title)

        self.driver.refresh()
        title = self.driver.title
        self.assertEqual("Index of Available Pages", title)
if __name__ == '__main__':
    unittest.main()
