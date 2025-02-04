import unittest
import sys
sys.path.append('tests/python')
from base_firefox_test import BaseFirefoxTest
from selenium.webdriver.common.by import By

class InformationTests(BaseFirefoxTest):

    def test_informarion(self):
        self.driver.implicitly_wait(0.5)
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # isDisplayed
        is_email_visible = self.driver.find_element(By.NAME, "email_input").is_displayed()
        self.assertTrue(is_email_visible)

        # isEnabled
        is_enabled_button = self.driver.find_element(By.NAME, "button_input").is_enabled()
        self.assertTrue(is_enabled_button)

        # isSelected
        is_selected_check = self.driver.find_element(By.NAME, "checkbox_input").is_selected()
        self.assertTrue(is_selected_check)

        # TagName
        tag_name_inp = self.driver.find_element(By.NAME, "email_input").tag_name
        self.assertTrue(tag_name_inp)

        # GetRect
        rect = self.driver.find_element(By.NAME, "range_input").rect
        self.assertEqual(10, rect["x"])

        # CSS Value
        css_value = self.driver.find_element(By.NAME, "color_input").value_of_css_property(
            "font-size"
        )
        self.assertEqual("13.3333px", css_value)

        # GetText
        text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Testing Inputs", text)

        # FetchAttributes
        email_txt = self.driver.find_element(By.NAME, "email_input")
        value_info = email_txt.get_attribute("value")
        self.assertEqual("admin@localhost", value_info)

if __name__ == '__main__':
    unittest.main()
