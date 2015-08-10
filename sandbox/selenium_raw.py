#! python
__author__ = 'John Underwood'

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("hello")
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")  # check in later JNU!!!
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Common/chromedriver',
                          chrome_options=chrome_options)

# Optional argument, if not specified will search path.
# driver = webdriver.Chrome('C:/Common/chromedriver')
driver.get('http://indytest')
print(driver.title)
assert "INDY" in driver.title
time.sleep(3)  # Let the user actually see something!

element = driver.find_element_by_xpath(
    '//*[@id="slide-out"]/li[5]/ul/li/a/i')
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(
    '//*[@id="slide-out"]/li[5]/ul/li/div/ul/li[1]/a')
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(  # click 'All' link
    '//*[@id="checklist-form-container"]/div[1]/a')
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(  # click provider's link
    '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[3]/td[3]/a')
element.click()
time.sleep(1)
print("Check HERE")

for handle in driver.window_handles:
    driver.switch_to.window(handle)

element = driver.find_element_by_xpath(  # click provider's examinations
    '//*[@id="content"]/div[2]/div[1]/ul/div/a[3]')
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(  # click add examination
    '//*[@id="examinationGrid_form"]/a[1]')
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(  # click passed checkbox
    '//*[@id="examinationEdit_form"]/div[1]/div/div[1]/div/label')
element.click()

# element.send_keys('ChromeDriver')
# element.submit()
# time.sleep(3)  # Let the user actually see something!
# element = driver.find_element_by_id('lst-ib')
# element.clear()
# element.send_keys('Python')
# time.sleep(1)
# element.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
