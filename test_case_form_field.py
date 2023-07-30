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
# Note: On my computer, the website takes a lot of time to load, adjust based on your connection.
driver.implicitly_wait(15)

# find the modal and close it
driver.find_element(By.XPATH, "//span[@role='presentation']").click()


# find from field and click
from_field = driver.find_element(
    By.XPATH, "//div[@class='sc-12foipm-35 eZvdEH']//p[@class='sc-12foipm-20 hKRKsX'][normalize-space()='Enter city or airport']").click()

# send keys to activated form field
form_field_active = driver.find_element(
    By.XPATH, "//input[@type='text']").send_keys("New York")

# Find the dropdown menu
drop_down_menu = driver.find_element(
    by=By.XPATH, value="//body/div[@id='root']/div[@class='sc-1gt8xf5-0 cEQQxj']/div[@class='sc-1gt8xf5-3 gWnzGY']/div[@class='sc-12foipm-30 fPhIcX']/div[@class='sc-12foipm-14 IAfj']/div[@class='sc-12foipm-34 keCaow']/div[@class='sc-12foipm-35 eZvdEH']/div[@class='sc-12foipm-37 idMXOL']/ul[@id='autoSuggest-list']/li[4]/div[1]").click()

# wait for 3 seconds to see the selection
time.sleep(3)

# Close browser
driver.quit()
