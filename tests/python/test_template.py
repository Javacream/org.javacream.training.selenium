import unittest
import sys
sys.path.append('tests/python')
from base_firefox_test import BaseFirefoxTest
from selenium.webdriver.common.by import By

class Test(BaseFirefoxTest):
    pass

if __name__ == '__main__':
    unittest.main()
