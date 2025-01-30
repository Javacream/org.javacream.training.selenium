from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Open the browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Enter username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!" + Keys.RETURN)

# Verify login success
message = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in message
print(message)
# Close browser
driver.quit()
