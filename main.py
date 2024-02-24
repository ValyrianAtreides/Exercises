from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from data import data


chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
for entry in data:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        "https://docs.google.com/forms/d/1t7dqUKSsnO1MMXVD48DJP_Kpx-6cWMMjnyw-7tntwZQ/viewform?edit_requested=true")
    sleep(2)
    time_form = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_form = driver.find_element(By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_form = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    timestamp = entry['Timestamp']
    address = entry['Address']
    rent = entry['Rents']
    link = entry['Link']


    address_form.send_keys(address)


    rent_form.send_keys(rent)


    link_form.send_keys(link)


    time_form.send_keys(timestamp)

    submit_button.click()
    driver.close()

