from selenium import webdriver
import os
import time
 
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#os.environ['PATH'] += r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\SelniumDrivers"
driver = webdriver.Chrome(executable_path=r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\chromedriver.exe",chrome_options=options)
#driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)


#login
username = driver.find_element(by=By.ID,value='Frm_Username')
username.send_keys()
    
LastPassword = driver.find_element(by=By.ID,value='Frm_Password')
LastPassword.send_keys("")
    
time.sleep(2)
button1 = driver.find_element(by=By.XPATH,value='//*[@id="LoginId"]')
button1.click()
#processus de changement du password1
button2 = driver.find_element(by=By.XPATH,value='//*[@id="localnet"]')
button2.click()
button3 = driver.find_element(by=By.XPATH,value='//*[@id="wlanConfig"]')
button3.click()
button4 = driver.find_element(by=By.XPATH,value='//*[@id="WLANSSIDConfBar"]')
button4.click()
#For 5G
NewPassword1 = driver.find_element(by=By.XPATH,value='//*[@id="KeyPassphrase:0"]')
NewPassword1.clear()
NewPassword1.send_keys("")
button6 = driver.find_element(by=By.XPATH,value='//*[@id="Btn_apply_WLANSSIDConf:0"]')
button6.click()
time.sleep(2)


button5 = driver.find_element(by=By.XPATH,value='//*[@id="instName_WLANSSIDConf:4"]')
button5.click()
#For 4G
NewPassword2 = driver.find_element(by=By.XPATH,value='//*[@id="KeyPassphrase:4"]')
NewPassword2.clear()
NewPassword2.send_keys("")
button6 = driver.find_element(by=By.XPATH,value='//*[@id="Btn_apply_WLANSSIDConf:4"]')
button6.click()
#logout
time.sleep(2)
button6 = driver.find_element(by=By.XPATH,value='//*[@id="LogOffLnk"]')
button6.click()
time.sleep(10)