import unittest
import sys
sys.path.append('tests/python')

from base_firefox_test import BaseFirefoxTest

class TestDemo(BaseFirefoxTest):
  
  def test_title_is_Javacream(self):
    self.driver.get("http://javacream.org/")
    self.driver.set_window_size(1120, 692)
    self.assertEqual('Javacream', self.driver.title)

if __name__ == '__main__':
  unittest.main()
