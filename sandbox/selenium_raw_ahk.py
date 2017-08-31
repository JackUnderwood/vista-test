#! python
import time
# import ctypes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


__author__ = 'John Underwood'
""" AutoHotkey (AHK)
https://autohotkey.com/docs/Tutorial.htm

Don't need to use AHK, because the driver provides the switch_to.alert function.
"""

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

driver.get('http://indytest/jobs/search')
driver.implicitly_wait(2)
print(driver.title)

element = driver.find_element_by_id('s_job_number')
element.send_keys("92118")

element = driver.find_element_by_css_selector(
    '#job-search-wrap>div:nth-child(3)>div:nth-child(2)>button')
element.click()  # Lic Info - Examinations link

element = driver.find_element_by_id('edit_92118')
element.click()  # Click row's edit button

element = driver.find_element_by_id('reason-do-not-post')
select = Select(element)  # Edit Job's "Reason not to post"
select.select_by_visible_text("Job is a duplicate")

time.sleep(2)
element = driver.find_element_by_id('drawer-close')
element.click()  # Click drawer's cancel button


time.sleep(2)
alert = driver.switch_to.alert
alert_text = alert.text
print("The alert states: {}".format(alert_text, ))
msg = 'Are you sure you want to lose your work?'
if alert_text != '' and msg in alert_text:
    driver.switch_to.alert.dismiss()  # switch_to() avoids the need to use AHK

time.sleep(2)

# https://sjohannes.wordpress.com/2012/03/23/win32-python-getting-all-window-titles/
# EnumWindows = ctypes.windll.user32.EnumWindows
# EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),
#                                      ctypes.POINTER(ctypes.c_int))
# GetWindowText = ctypes.windll.user32.GetWindowTextW
# GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
# IsWindowVisible = ctypes.windll.user32.IsWindowVisible
#
# titles = []
# d = {}
#
#
# def foreach_window(hwnd, lparam):
#     if IsWindowVisible(hwnd):
#         length = GetWindowTextLength(hwnd)
#         buff = ctypes.create_unicode_buffer(length + 1)
#         GetWindowText(hwnd, buff, length + 1)
#         time.sleep(0.2)
#         d[buff.value] = hwnd
#         titles.append(buff.value)
#     return True
# EnumWindows(EnumWindowsProc(foreach_window), 0)
#
# print(titles)
# print(d['Open'])  # holds the window handle to the Open window
# time.sleep(3)
# # Now, let's manipulate the 'Open' window.
# open_window = None
# if 'Open' in d:
#     open_window = d['Open']
#     # We've got the win object, let's click the Cancel button


time.sleep(5)  # Gives us time to see something!
driver.quit()
