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

from tool.vlog import VLog

log = VLog(name="vtf", log_name="UI")


# TODO: fix selenium logging to not display at DEBUG level
# from selenium.webdriver.remote.remote_connection import LOGGER
# LOGGER.setLevel(log.WARNING)


class UI:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome('C:/Common/chromedriver',
                              chrome_options=chrome_options)
    driver.implicitly_wait(5)  # seconds
    driver.get('http://oasslcvswebt01')  # http://dev.com
    assert "INDY" in driver.title

    runtime = {}
    override = {}
    element = None  # TODO: the driver's element

    def __init__(self, override=None):
        self.override = override
        log.debug("UI __init__()")

    def update(self, runtime):
        log.debug("update()")
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
        log.debug("execute()")
        for item in items:
            t = self.runtime.get(item, ("Unknown", "Unknown", "Unknown"))
            # print(t)
            command, element, value = t
            if command == "Click":
                self.click(element)
            elif command == "Type":
                self.type(element, value)
            elif command == "Find":
                self.find(element, value)
            elif command == "Select":
                self.select(element, value)
            elif command == "Wait":
                self.wait_for_element(element, value)
            elif command == "Unknown":
                print("This command is unknown - throw an error")
            else:
                print("Throw an error")
            # print()
            time.sleep(1)
        # self.driver.quit() # JNU have driver quit during teardown

    def chain(self, paths):

        pass

    def click(self, elem):
        # value = "nicely done"
        log.info("Click Command - PATH: \'{0}\'".format(elem))
        element = self.find_element(elem)
        element.click()

    def type(self, elem, value):
        log.info("Type Command - PATH: \'{0}\' - VALUE: {1}".format(elem, value))
        element = self.find_element(elem)
        element.send_keys(value)
        element.submit()

    def find(self, elem, value):
        """
        Special 'Type' case for Find... that requires no submit()
        :param elem:
        :param value:
        :return:
        """
        log.info("Type Command for Find... - PATH: \'{0}\' - VALUE: {1}".
                 format(elem, value))
        element = self.find_element(elem)
        element.send_keys(value)

    def select(self, elem, value):
        """
        May want to add the other options such as by value and by index.
        See http://selenium-python.readthedocs.org/en/latest/api.html
        :param elem: holds the xpath, id, or class
        :param value: visible text inside the list
        :return: void
        """
        log.info("Select Command - PATH: {0} - VALUE: {1}".format(elem, value))
        element = self.find_element(elem)
        select = Select(element)
        select.select_by_visible_text(value)

    def wait_for_element(self, elem_id, wait_time):
        log.info("Wait Command - wait for id=\"{0}\"".format(elem_id))
        from selenium.webdriver.support import expected_conditions as ec
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        try:
            WebDriverWait(self.driver, wait_time).until(
                ec.presence_of_element_located((By.ID, elem_id))
            )
        finally:
            pass

    def find_element(self, elem):
        """
        :param elem: a valid selector type, ie. xpath, class, or id
        :return: the DOM's element
        """
        first_element = elem[0]
        if first_element == '/':  # xpath
            return self.driver.find_element_by_xpath(elem)
        elif first_element == '.':  # class
            _class = elem[1:]
            return self.driver.find_element_by_class_name(_class)
        elif first_element == '#':  # id
            _id = elem[1:]
            return self.driver.find_element_by_id(_id)
        else:
            # TODO: need to throw excp
            log.exception("no correct element found")

        return None

    def teardown(self):
        # TODO: this should also be in the launch file vtf
        log.info("Teardown")
        self.wait(1)  # Remove later JNU!!!
        self.driver.quit()

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
