import unittest
import sys
sys.path.append('tests/python')

from challenging_dom_page import ChallengingPage
class ChallengingTest(unittest.TestCase):
  def setUp(self):
    self.page = ChallengingPage()
  def tearDown(self):
    self.page.close()    

  def test_title(self):
    self.assertIn('The Internet', self.page.get_title())

  def test_get_blue_button(self):
    print([element.get_attribute("class") for element in self.page.get_blue_button()])

if __name__ == '__main__':
  unittest.main()
