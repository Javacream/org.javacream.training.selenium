from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox as Browser
def local():
    geckodriver_path = "/snap/bin/geckodriver"
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver_service = webdriver.FirefoxService(options=options, executable_path=geckodriver_path)

    driver = Browser(service=driver_service)
    return driver

def grid():
    options = Options()
    driver = webdriver.Remote(command_executor='http://javacream.eu:4444', options=options)
    return driver

