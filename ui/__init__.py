__author__ = 'John Underwood'
"""
This class will setup the selenium driver and process all commands from
subclasses. This class drives the user interface testing framework.

Selectors Reference:
//xpath
.class
#id
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from colorama import init, Fore


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
    element = None  # TODO: the driver's element

    def __init__(self, override=None):
        init()  # init the colorama stuff
        self.override = override
        print("UI __init__")

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
        Note: 'item' always expects a tuple of three elements
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
        print(Fore.CYAN + "Click command" + Fore.RESET)
        print(Fore.CYAN + ">>> PATH: %s " + Fore.RESET % path)
        element = self.find_element(path)
        element.click()

    def type(self, path, value):
        print(Fore.CYAN + "Type command" + Fore.RESET)
        print(Fore.CYAN + ">>> PATH: %s \n>>> VALUE: %s" + Fore.RESET %
              (path, value))
        element = self.find_element(path)
        element.send_keys(value)
        element.submit()

    def select(self, path, value):
        """
        May want to add the other options such as by value and by index.
        See http://selenium-python.readthedocs.org/en/latest/api.html
        :param path: holds the xpath, id, or class
        :param value: visible text inside the list
        :return: void
        """
        print(Fore.CYAN + "Select command" + Fore.RESET)
        print(Fore.CYAN + ">>> PATH: %s \n>>> VALUE: %s" + Fore.RESET %
              (path, value))
        element = self.find_element(path)
        select = Select(element)
        select.select_by_visible_text(value)

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
            # TODO: need to throw excp
            print(Fore.RED + "error: no correct element found" + Fore.RESET)

        return None

    def teardown(self):
        # TODO: this should also be in the launch file vtf
        time.sleep(5)  # Remove later JNU!!!
        self.driver.quit()

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
