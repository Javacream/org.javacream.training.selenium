import unittest
import driver_configuration as config
class BaseFirefoxTest(unittest.TestCase):
  def setUp(self):
    self.driver = config.grid()
  
  def tearDown(self):
    self.driver.quit()
  
