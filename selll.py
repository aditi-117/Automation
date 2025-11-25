from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Make sure you have the appropriate WebDriver installed and in your PATH (e.g., ChromeDriver)
driver = webdriver.Chrome()
try:
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("MR BEAST")
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)  # Wait to see results
finally:
    driver.quit()
# For educational purposes only. Always comply with YouTube's Terms of Service when using automation.
