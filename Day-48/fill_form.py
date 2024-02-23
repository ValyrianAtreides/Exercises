from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname=driver.find_element(By.NAME, value="fName")
fname.send_keys("Berkay",Keys.ENTER)

lname=driver.find_element(By.NAME, value="lName")
lname.send_keys("Aydın",Keys.ENTER)

mail=driver.find_element(By.NAME, value="email")
mail.send_keys("berkayhede@gmail.com",Keys.ENTER)