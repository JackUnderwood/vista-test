#! python
# import re
import time
# import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By


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
driver.get('http://indytest/jobs/search')
time.sleep(2)

status = driver.find_element_by_css_selector(
    '.ui-multiselect.ui-widget.ui-state-default.ui-corner-all.'
    'multi_s.multi_s_job_status')
status.click()
time.sleep(1)

active = driver.find_element_by_id('ui-multiselect-s_job_status-option-1')
active.click()
hot = driver.find_element_by_id('ui-multiselect-s_job_status-option-4')
hot.click()
time.sleep(3)

# Find the items that have set 'Ready to Post? No'
# //*[@id="expandable_97867"]/td/div/div[3]/div[2]/div[4]/div/div/div[2]
# //*[@id="expandable_97866"]/td/div/div[3]/div[2]/div[4]/div/div/div[2]
# //*[@id="expandable_97866"]/td/div/div[3]/div[2]/div[4]/div/div/div[2]/strong
# //*[@id="expandable_97866"]/td/div/div[3]/div[3]/div[2]/div/div/div/div[2]/strong
# table = driver.find_element_by_xpath('//*[@id="result-target"]/tbody')

rows = driver.find_elements_by_xpath(
    '//*[@id="result-target"]/tbody/tr[@class=" " or @class="odd "]')
valid_rows = [row.find_element_by_xpath('./td[1]').text for row in rows]
# for row in rows:
#     row_id = row.find_element_by_xpath('./td[1]').text
#     valid_rows.append(row_id)

# //*[@id="expandable_97866"] #result-target > tbody > tr:nth-child(1)
print(valid_rows)
time.sleep(5)
driver.quit()

