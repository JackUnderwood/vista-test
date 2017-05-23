#! python
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

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

# Find the background color
job_number = driver.find_element_by_id('s_job_number')
job_number.send_keys('97864')  # 97867

search = driver.find_element_by_xpath(
    '//*[@id="job-search-wrap"]/div[2]/div[2]/button')
search.click()

row = driver.find_element_by_xpath('//*[@id="result-target"]/tbody/tr[1]')
rgb = row.value_of_css_property('background-color')
res = re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+)', rgb).group()
r, g, b = [int(s) for s in re.findall('\\d+', res)]
hex_color = '#%02x%02x%02x' % (r, g, b)


time.sleep(5)  # Let the user see something!
driver.quit()

