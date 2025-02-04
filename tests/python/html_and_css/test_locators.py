import unittest
import sys
sys.path.append('tests/python')
from base_firefox_test import BaseFirefoxTest
from selenium.webdriver.common.by import By

class LocatorTests(BaseFirefoxTest):

    def setUp(self):
        super().setUp()
        self.driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")

    def test_class_name(self):
        element = self.driver.find_element(By.CLASS_NAME, "information")
        self.assertIsNotNone(element)
        self.assertEqual("input", element.tag_name)

    def test_css_selector(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "#fname")
        self.assertIsNotNone(element)
        self.assertEqual("Jane", element.get_attribute("value"))


    def test_id(self):
        element = self.driver.find_element(By.ID, "lname")

        self.assertIsNotNone(element)
        self.assertEqual("Doe", element.get_attribute("value"))

    def test_name(self):
        element = self.driver.find_element(By.NAME, "newsletter")
        self.assertIsNotNone(element)
        self.assertEqual("input", element.tag_name)


    def test_link_text(self):
        element = self.driver.find_element(By.LINK_TEXT, "Selenium Official Page")

        self.assertIsNotNone(element)
        self.assertEqual("https://www.selenium.dev/", element.get_attribute("href"))

    def test_partial_link_text(self):
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")

        self.assertIsNotNone(element)
        self.assertEqual("https://www.selenium.dev/", element.get_attribute("href"))

    def test_tag_name(self):
        element = self.driver.find_element(By.TAG_NAME, "a")

        self.assertIsNotNone(element)
        self.assertEqual("https://www.selenium.dev/", element.get_attribute("href"))

    def test_xpath(self):
        element = self.driver.find_element(By.XPATH, "//input[@value='f']")
        self.assertIsNotNone(element)
        self.assertEqual("radio", element.get_attribute("type"))

if __name__ == '__main__':
    unittest.main()
