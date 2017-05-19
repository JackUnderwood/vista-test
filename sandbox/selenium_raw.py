#! python
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

__author__ = 'John Underwood'

print("hello")
chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("window-size=1280,1024")
chrome_options.add_argument("--disable-extensions")  # developer extensions
chrome_options.add_argument("--disable-gpu")
# This option takes care of a known issue in the browser, where the
# PDF viewer does not function as expected--it downloads the file.
chrome_options.add_experimental_option(
    'excludeSwitches',
    ['test-type', 'ignore-certificate-errors'])

driver = webdriver.Chrome('C:/Common/chromedriver',
                          chrome_options=chrome_options)
driver.implicitly_wait(5)
driver.get('http://indytest')
time.sleep(2)

# Explicit waits -- wait for <title> to change
directory = driver.find_element_by_id('button_employee_directory')
directory.click()

name = driver.find_element_by_xpath(
    '//*[@id="employeeDirectoryMini_grid"]/tfoot/tr/th[3]/input')
name.send_keys("Underwood")

edit = driver.find_element_by_xpath(  # This drawer takes forever to pull up!!!
    '//*[@id="employeeDirectoryMini_grid"]/tbody/tr/td[10]/a/i')
edit.click()

# Add explicit wait HERE -- wait for drawer to appear
title = ' (John Underwood) Manage User'
wait = WebDriverWait(driver, 20)
try:
    wait.until(lambda x: title in driver.title)
except TimeoutException as te:
    pass

company = driver.find_element_by_xpath(
    '//*[@id="manageUser_form"]/div[2]/div[1]/ul/li[3]')
company.click()

time.sleep(5)  # Let the user see something!
driver.quit()

