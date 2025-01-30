from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class SearchPage():
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='searchbox_homepage']//*[@type='submit']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.url = "https://duckduckgo.com/"

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))

    def make_a_search(self, input_text):
        search_input = self.wait.until(EC.visibility_of_element_located(SearchPage.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(input_text)

        search_button = self.wait.until(EC.element_to_be_clickable(SearchPage.SEARCH_BUTTON))
        search_button.click()

        self.wait.until(EC.presence_of_all_elements_located(SearchPage.RESULTS))
        print(self.driver.save_screenshot("results/results.png"))