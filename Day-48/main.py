from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


menu=driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text

lines = menu.splitlines()

event_dict={}

for i in range(0, len(lines), 2):  #2 yaptık çünkü ilk önce 0'ı sonra 1'i sonraki döngüde ise 2'yi ve 3'ü alacak
    date = lines[i]
    event_name = lines[i+1]
    event_dict[len(event_dict)] = {"Date": date, "Event Name": event_name}

print(event_dict)

#event_times=driver.find_element(By.CSS_SELECTOR,value=".event-widget time")
#event_times=driver.find_element(By.CSS_SELECTOR,value=".event-widget li a")

#for n in range(len(event_times)):
#    events[n]={
#        "Time":event_times[n].text,
#        "Name":event_names[n].text
#}