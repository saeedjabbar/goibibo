# importing time module
import time

# importing selenium webdriver and By class
from selenium import webdriver
from selenium.webdriver.common.by import By

# setting up chrome driver
driver = webdriver.Chrome()

# opening the website
driver.get("https://www.goibibo.com/")

# wait for DOM to load
# Note: On my computer, the website takes a lot of time to load.
driver.implicitly_wait(25)

# find the modal and close it
driver.find_element(By.XPATH, "//span[@role='presentation']").click()


# find from field and click
from_field = driver.find_element(
    By.XPATH, "//div[@class='sc-12foipm-34 dVpEne']//p[@class='sc-12foipm-27 bhYNaI fswWidgetPlaceholder'][normalize-space()='Enter city or airport']").click()

# send keys to activated form field
form_field_active = driver.find_element(
    By.XPATH, "//div[@class='sc-12foipm-37 godvBN']//input").send_keys("New York")

# wait for 3 seconds
time.sleep(3)

# from_field.send_keys("New York")

# Send New York data to the From field
# from_field.send_keys("New York")

# wait for 3 seconds
time.sleep(3)

# Close browser
driver.quit()

# # check if login was successful with basic logging
# if driver.current_url == "https://www.saucedemo.com/inventory.html":
#     print("Login successful!")
# else:
#     print("Login failed!")
