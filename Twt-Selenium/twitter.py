from selenium import webdriver
from getpass import getpass
import time

usr = raw_input('Enter your username or email : ')
pwd = getpass('Enter your password : ')

driver = webdriver.Chrome ()
driver.get('https://twitter.com/login')

email_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
login_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div'

usr_box = driver.find_element_by_xpath(email_xpath)
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_xpath(password_xpath)
pwd_box.send_keys(pwd)

login_button_element = driver.find_element_by_xpath(login_button_xpath)
time.sleep(1)
login_button_element.click()
