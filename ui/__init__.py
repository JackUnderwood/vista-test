__author__ = 'John Underwood'
"""
This is an abstract class that will setup the selenium driver and process all
commands from subclasses. This drives the user interface testing framework.

Selectors Reference:
//xpath
.class
#id
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class UI:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome('C:/Common/chromedriver',
                              chrome_options=chrome_options)
    driver.implicitly_wait(5)  # seconds
    driver.get('http://dev.com')
    assert "INDY" in driver.title

    runtime = {}
    override = {}
    element = None  # the driver's element  TODO:

    def __init__(self, override=None):
        self.override = override
        print("UI __init__", override)

    def update(self, runtime):
        print("UI update()")
        if self.override:
            # override the 'passed in' runtime data
            runtime.update(self.override)
        self.runtime.update(runtime)

    def execute(self, items):
        """
        :param items: a dictionary of tuples
        :return: void
        # 'item' always expects a tuple of three elements
        """
        for item in items:
            t = self.runtime.get(item, ("Unknown", "Unknown", "Unknown"))
            print(t)
            command, path, value = t
            if command == "Click":
                self.click(path)
            elif command == "Type":
                self.type(path, value)
            elif command == "Select":
                self.select(path, value)
            elif command == "Unknown":
                print("This command is unknown - throw an error")
            else:
                print("Throw an error")
            print()
            time.sleep(1)
        # self.driver.quit() # JNU have driver quit during teardown

    def click(self, path):
        print("This is a Click command")
        print("PATH is", path)
        element = self.find_element(path)
        element.click()

    def type(self, path, value):
        print("This is a Type command")
        print("PATH and VALUE is", path, value)
        element = self.find_element(path)
        element.send_keys(value)
        element.submit()

    def select(self, path, value):
        print("This is a Select command")
        print("PATH and VALUE is", path, value)
        self.find_element(path)  # TODO: needs to be implemented

    def find_element(self, path):
        """
        :param path: a valid selector type, ie. xpath, class, or id
        :return: the DOM's element
        """
        first_element = path[0]
        if first_element == '/':  # xpath
            return self.driver.find_element_by_xpath(path)
        elif first_element == '.':  # class
            _class = path[1:]
            return self.driver.find_element_by_class_name(_class)
        elif first_element == '#':  # id
            _id = path[1:]
            return self.driver.find_element_by_id(_id)
        else:
            print("error: no correct element found")  # TODO: need to throw excp

        return None

    def teardown(self):  # TODO: this should also be in the launch file vtf
        time.sleep(5)  # Remove later JNU!!!
        self.driver.quit()

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
