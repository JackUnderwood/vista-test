#! python
import time
import ctypes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


__author__ = 'John Underwood'
""" AutoHotkey (AHK)
https://autohotkey.com/docs/Tutorial.htm
"""

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

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),
                                     ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
d = {}


def foreach_window(hwnd, lparam):
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


time.sleep(5)  # Let the user actually see something!
driver.quit()
