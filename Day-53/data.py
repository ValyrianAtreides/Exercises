from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


response=requests.get("https://appbrewery.github.io/Zillow-Clone/")
web_page=response.text

soup=BeautifulSoup(web_page,"html.parser")

addresses=[]
rents=[]
links=[]
dates=[]
address_elements = soup.find_all("address")

for element in address_elements:
    addresses.append(element.get_text(strip=True))

address_list = "\n".join(addresses).splitlines()

rent_prices=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")

for price in rent_prices:
    current_time=datetime.now()
    formatted_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
    dates.append(formatted_time)
    if "+" in price.get_text():
        rents.append(price.get_text().split("+")[0])
    else:
        rents.append(price.get_text().split("/")[0])


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/Zillow-Clone/")

li_elements=driver.find_elements(By.XPATH,value='//*[@id="grid-search-results"]/ul/li')


for li_element in li_elements:
    li_element.click()
    links.append(driver.current_url)
    driver.back()

driver.quit()

data=[]

for ts, address, rent, link in zip(dates, address_list, rents, links):
    entry = {'Timestamp': ts, 'Address': address,'Rents': rent,'Link':link}
    data.append(entry)

print(data)


