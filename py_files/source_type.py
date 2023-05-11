import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui, sys
import mouse
import requests

# Send Notifications 

# Open Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.annotations.attentive.ai")   


# Login annotations 
email = driver.find_element(By.XPATH,'/html/body/div/div/section/div/div[2]/div/div/form/input')
email.click()
email.send_keys('raghav.narula@attentive.ai')

pwd = driver.find_element(By.XPATH,'/html/body/div/div/section/div/div[2]/div/div/form/span/input')
pwd.click()
pwd.send_keys('Password!123')

driver.find_element(By.XPATH,'/html/body/div/div/section/div/div[2]/div/div/form/button').click()


time.sleep(5)

driver.get('https://qa.annotations.attentive.ai/management/source-type')


## Add and Delete Source Type ...
source_type_name = "tester"


time.sleep(1)
# Open Add source type popup
add_source_type = driver.find_element(By.XPATH,'//span[text()="Add Source Type"]/..')
add_source_type.click()

# Enter the Source name and Click Submit..
enter_source_name = driver.find_element(By.XPATH,'//input[@placeholder="Enter source name..."]')
time.sleep(1)
enter_source_name.click()
enter_source_name.send_keys(f'{source_type_name}')

submit_button = driver.find_element(By.XPATH,'//span[text()="Submit"]')
submit_button.click()

print("New Source Type Created")


### Open Add Source type PopUp ###
add_source_type = driver.find_element(By.XPATH,'//span[text()="Add Source Type"]/..')
time.sleep(1)
add_source_type.click()




#### Repeating with same source type.. to check if same source type is allowed or not.. #####

enter_source_name = driver.find_element(By.XPATH,'//input[@placeholder="Enter source name..."]')
time.sleep(1)
enter_source_name.click()
enter_source_name.send_keys(f'{source_type_name}')

submit_button = driver.find_element(By.XPATH,'//span[text()="Submit"]')
time.sleep(1)
submit_button.click()
time.sleep(1)

try:
    toast_msg = driver.find_element(By.XPATH,'//span[text()="Source Type with this Source Type already exists."]')
    print("Toast Message Source Type with this Source Type already exists Appears.")
except:
    print("Toast Message is not coming..")




###### Delete Source Type (Take Me Back) ######
time.sleep(2)
delete_source_name = driver.find_element(By.XPATH,f'//tr[@data-row-key="{source_type_name}"]/td[2]/button') # delete button
time.sleep(1)
delete_source_name.click()

# Dialog box must open
type_in = driver.find_element(By.XPATH,'//small[text()="Type exactly the same name with same case & spacing."]/../input')
time.sleep(1)
type_in.click()
type_in.send_keys(source_type_name)

try:
    click_delete_button = driver.find_element(By.XPATH,'//span[text()="Take me back"]/..')
    time.sleep(2)
    click_delete_button.click()
    print("Take Me Back Working")

except:
    print("Take Me back Not Working")



#### Delete Source Type(writing wrong name) ####
time.sleep(1)
delete_source_name = driver.find_element(By.XPATH,f'//tr[@data-row-key="{source_type_name}"]/td[2]/button') # delete button
time.sleep(1)
delete_source_name.click()

# Dialog box must open
type_in = driver.find_element(By.XPATH,'//small[text()="Type exactly the same name with same case & spacing."]/../input')
time.sleep(1)
type_in.click()
type_in.send_keys("Wrong Data")
time.sleep(2)

click_delete_button = driver.find_element(By.XPATH,'//span[text()="Delete Source Type"]/..')
time.sleep(1)
click_delete_button.click()
time.sleep(1)

try:
    toast_msg = driver.find_element(By.XPATH,'//span[text()="Please type the exact name."]')
    print("Toast Message -> \"Please type the exact name\" Appears")
except:
    print("Toast Message is not coming..")

# Close the Pop Up
close_button = driver.find_element(By.XPATH,f'//div[text()="Delete {source_type_name}?"]/../../button/span/span')
time.sleep(0.5)
close_button.click()

##### Delete a Source Type (Successful one..) #####
time.sleep(2)
delete_source_name = driver.find_element(By.XPATH,f'//tr[@data-row-key="{source_type_name}"]/td[2]/button') # delete button
time.sleep(1)
delete_source_name.click()

# Dialog box must open
type_in = driver.find_element(By.XPATH,'//small[text()="Type exactly the same name with same case & spacing."]/../input')
time.sleep(1)
type_in.click()
type_in.send_keys(source_type_name)

click_delete_button = driver.find_element(By.XPATH,'//span[text()="Delete Source Type"]/..')
time.sleep(1)
click_delete_button.click()
