from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

button=driver.find_element(By.CSS_SELECTOR,value="#cookie")

for i in range(1000):
    button.click()
