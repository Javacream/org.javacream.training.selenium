import unittest
import sys
sys.path.append('tests/python')
from base_firefox_test import BaseFirefoxTest
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC

class WaitTest(BaseFirefoxTest):
    def test_explicit(self):
        self.driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
        revealed = self.driver.find_element(By.ID, "revealed")
        self.driver.find_element(By.ID, "reveal").click()

        # wait = WebDriverWait(self.driver, timeout=0.1) # TimeoutException
        wait = WebDriverWait(self.driver, timeout=2)
        wait.until(lambda d : revealed.is_displayed())

        revealed.send_keys("Displayed")
        self.assertEqual("Displayed", revealed.get_property("value"))

    def xtest_explicit_ec(self):
        self.driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
        self.driver.find_element(By.ID, "reveal").click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, "revealed")))
        revealed = self.driver.find_element(By.ID, "revealed")
        revealed.send_keys("Displayed")
        self.assertEqual("Displayed", revealed.get_property("value"))

if __name__ == '__main__':
    unittest.main()