from base_firefox_test import BaseFirefoxTest
import unittest
from duckduckgo_search_page import SearchPage
class DuckduckgoTest(BaseFirefoxTest):
  
  def test_title_is_DuckDuckGo(self):
    search_page = SearchPage(self.driver)
    self.assertIn('DuckDuckGo', search_page.get_title())

  def test_search(self):
    search_page = SearchPage(self.driver)
    search = "Selenium Tests"
    search_page.make_search(search)
if __name__ == '__main__':
  unittest.main()
