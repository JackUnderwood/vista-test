#! python
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


__author__ = 'John Underwood'

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
    'http://indytest/checklist/checklist/checklist/71/entity/574458/inline/1/')
print(driver.title)

element = driver.find_element_by_css_selector(
    '#content>div.row>div.col.s3>ul>div>a:nth-child(3)')
element.click()  # Lic Info - Examinations link
element = driver.find_element_by_css_selector(
    '#ribbon_form>ul>li>div.collapsible-body>div:nth-child(5)>'
    'div.col.s6.right-buttons.right-align>a:nth-child(2)')
time.sleep(3)
element.click()  # ribbon's Malpractice button
element = driver.find_element_by_css_selector(
    '#experienceUpload>div>div.FWUploadDropZone>i.fa-stack.fa.fa-cloud-upload')
time.sleep(2)
element.click()  # malpractice's drawer's upload cloud

time.sleep(3)

# https://sjohannes.wordpress.com/2012/03/23/win32-python-getting-all-window-titles/
import ctypes

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
d = {}


def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        time.sleep(0.2)
        d[buff.value] = hwnd
        titles.append(buff.value)
    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)

print(titles)
print(d['Open'])  # holds the window handle to the Open window
time.sleep(3)
# Now, let's manipulate the 'Open' window.
open_window = None
if 'Open' in d:
    open_window = d['Open']
    # We've got the win object, let's click the Cancel button
    

# ==> Get an array of rows from a table using the <tr> tag *^*^*^*^*^*^*^*^*^*^*^
# driver.get(
#     'http://oasslcvsweb01.emsc.root01.org/checklist/'
#     'checklist/checklist/71/entity/156942/inline/1/')
# print(driver.title)
# element = driver.find_element_by_xpath(  # click email address icon
#     '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[3]/i')
# element.click()
# time.sleep(1)
#
# table = driver.find_element_by_id('emailGrid_grid')
# rows = table.find_elements_by_tag_name('tr')

# ==> Previous tests - reserve for future reference ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^
# from selenium.webdriver.support.ui import Select
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
