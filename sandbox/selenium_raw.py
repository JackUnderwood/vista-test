#! python
__author__ = 'John Underwood'

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

print("hello")
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")  # check in later JNU!!!
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Common/chromedriver',
                          chrome_options=chrome_options)
driver.implicitly_wait(5)

# Optional argument, if not specified will search path.
# driver = webdriver.Chrome('C:/Common/chromedriver')

# driver.get(
#     'http://indytest/checklist/checklist/checklist/71/entity/156942/inline/1/')
driver.get(
    'http://172.23.8.5/checklist/checklist/checklist/71/entity/156942/inline/1/')
print(driver.title)

time.sleep(3)

element = driver.find_element_by_xpath(  # click the ribbon
    '//*[@id="ribbon_form"]/ul/li/div[1]/div')
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(  # click email address icon
    '//*[@id="ribbon_form"]/ul/li/div[2]/div[3]/div[1]/a[3]/i')
element.click()
time.sleep(1)

table = driver.find_element_by_id('emailGrid_grid')
rows = table.find_elements_by_tag_name('tr')













# select = Select(element)
# select.select_by_visible_text('Provider Licensing')
# time.sleep(1)
#
# element = driver.find_element_by_id('template_id')
# select = Select(element)
# select.select_by_visible_text('License renewal')
# time.sleep(1)
#
# element = driver.find_element_by_id('desc_provider_id')
# element.send_keys('matt lambert st:wv')
#
# time.sleep(3)
# # click provider's name in Results
# element = driver.find_element_by_id('91273')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_id('license_id')
# select = Select(element)
# select.select_by_index(1)  # One-base index
# time.sleep(1)

# elements = driver.find_elements_by_xpath(
#     '//div[@id="add-recipient-container" and contains(@class, "find-form")]')

# for element in elements:
#     print(element)

# TROUBLE AREA ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^
# Need to find the input field
# Let's try finding all of them and then use the n element that applies here
# http://stackoverflow.com/questions/18570622/
#     selenium-and-xpath-finding-a-div-with-a-class-id-and-verifying-text-inside
# //div[contains(@class, 'Caption') and text()='Model saved']
# elements = driver.find_elements_by_class_name('find-form')

# element = driver.find_element_by_xpath(
#     '//*[@id="add-recipient-container"]/span[1]')  # Entity button
# element.click()
# time.sleep(1)
#
# elements = driver.find_elements_by_tag_name('input')  # too many objects
#
# element = elements[-1]
# print("AFTERWARDS")
#
# element.send_keys('matt lambert st:wv')
# time.sleep(2)
#
# element = driver.find_element_by_id('91273')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # Delivery Method
#     '//span[contains(@class, "type-title") and text()="Payroll Address"]')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # Save the delivery method
#     '//a[@button="save"]')
# element.click()
# time.sleep(1)
#
# # Add a User
# element = driver.find_element_by_xpath(
#     '//*[@id="add-recipient-container"]/span[2]')  # User button
# element.click()
# time.sleep(1)
#
# elements = driver.find_elements_by_tag_name('input')  # Here is the solution
#
# element = elements[-1]
# element.send_keys('Underwood')
# time.sleep(2)
#
# element = driver.find_element_by_id('1515')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # Save the delivery method
#     '//a[@button="save"]')
# element.click()
# time.sleep(1)


# element = driver.find_element_by_xpath(
#     '//*[@id="add-recipient-container"]/span[1]')  # Entity button
# element.click()
# time.sleep(1)
#
# elements = driver.find_elements_by_tag_name('input')  # too many objects
# element = elements[-1]
# time.sleep(1)
#
# element.send_keys('matt lambert st:wv')
# time.sleep(1)
#
# element = driver.find_element_by_id('91273')
# element.click()
# time.sleep(1)





# element = driver.find_element_by_xpath(
#     '//*[@id="slide-out"]/li[5]/ul/li/div/ul/li[1]/a')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # click 'All' link
#     '//*[@id="checklist-form-container"]/div[1]/a')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # click provider's link
#     '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[3]/td[3]/a')
# element.click()
# time.sleep(1)
# print("Check HERE")
#
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#
# element = driver.find_element_by_xpath(  # click provider's examinations
#     '//*[@id="content"]/div[2]/div[1]/ul/div/a[3]')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # click add examination
#     '//*[@id="examinationGrid_form"]/a[1]')
# element.click()
# time.sleep(1)
#
# element = driver.find_element_by_xpath(  # click passed checkbox
#     '//*[@id="examinationEdit_form"]/div[1]/div/div[1]/div/label')
# element.click()

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
