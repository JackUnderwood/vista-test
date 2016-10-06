#! python
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

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

# Click the Reset button
reset = driver.find_element_by_css_selector(
    '#job-search-wrap>div:nth-child(3)>div:nth-child(3)>button')
reset.click()
time.sleep(5)

element = driver.find_element_by_id('s_job_number')
element.clear()
element.send_keys('92116')
element.send_keys(Keys.ENTER)

element = driver.find_element_by_id('edit_92116')
element.click()

time.sleep(2)

reset = driver.find_element_by_css_selector(
    '#job-search-wrap>div:nth-child(3)>div:nth-child(3)>button')
try:
    reset.click()
except WebDriverException:
    pass

time.sleep(8)  # Let the user see something!
driver.quit()


