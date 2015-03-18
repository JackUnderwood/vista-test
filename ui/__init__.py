__author__ = 'John Underwood'
"""
This class will setup the selenium driver and process all commands from
subclasses. This class drives the user interface (UI) testing framework.

Selectors Reference:
//xpath
.class
#id
"""
import time
import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import tool.utilities as utils
from tool.vlog import VLog

log = VLog(name="vtf", log_name="UI")


class UI:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome('C:/Common/chromedriver',
                              chrome_options=chrome_options)
    driver.implicitly_wait(5)  # seconds
    test_url = utils.get_configurations("DEFAULT", "test_url")
    driver.get(test_url)  # http://oasslcvswebt01/
    assert "INDY" in driver.title

    pp = pprint.PrettyPrinter(indent=3)

    runtime = {}
    override = {}

    def __init__(self, override=None):
        """
        Takes a dictionary where its key(s) overrides a given key(s) inside
        'runtime' and the value replaces runtime's field set to '__OVERRIDE__'
        :param override: dict
        :return: void
        """
        self.override = override
        log.debug("UI __init__()")
        self.pp.pprint("OVERRIDE-> {}".format(self.override))

    def update(self, runtime):
        log.debug("update()")
        self.runtime.update(runtime)
        self.check_override()

    def execute(self, items):
        """
        :param items: a dictionary of tuples
        :return: void
        Note: 'item' always expects a tuple of three elements
        """
        log.debug("execute()")
        for item in items:
            t = self.runtime.get(item, ("Unknown", "Unknown", "Unknown"))
            command, element, value = t
            element = self.check_for_placeholder(command, element)

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
            elif command == "Chain":
                self.chain(element)
            elif command == "Unknown":
                print("This command is unknown - throw an error")
            else:
                print("Throw an error")
            time.sleep(1)

    def chain(self, elements):
        """
        Builds an 'action chain' - add more actions as needed - see link
        'http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver/
            selenium.webdriver.common.action_chains.html'
        :param elements: Contains a list of tuples; tuple structure is
        (action, {param1:p1, param2:p1}, (etc.), etc.)
        :return: void
        """
        actions = ActionChains(self.driver)
        # Build the actions chain
        for elem in elements:
            action, params = elem
            if action == "click":
                on_element = self.find_element(params['on_element'])
                actions.click(on_element)
            elif action == "click_and_hold":
                on_element = self.find_element(params['on_element'])
                actions.click_and_hold(on_element)
            elif action == "drag_and_drop":
                source = self.find_element(params['source'])
                target = self.find_element(params['target'])
                actions.drag_and_drop(source, target)
            elif action == "drag_and_drop_by_offset":
                source = self.find_element(params['source'])
                xoffset = params['xoffset']
                yoffset = params['yoffset']
                actions.drag_and_drop(source, xoffset, yoffset)
            elif action == "move_to_element":
                to_element = self.find_element(params['to_element'])
                actions.move_to_element(to_element)
            log.info("Chained action: {0}".format(action, ))
        actions.perform()

    def click(self, elem):
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
        Special 'Type' case for the 'Find...' that requires no submit()
        :param elem: the 'Find...' DOM element
        :param value: the search string
        :return: void
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
        """
        Waits for elements with the id attribute; id only
        :param elem_id: a string that holds the element's id
        :param wait_time: wait time in seconds
        :return: void
        """
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
        '//' for xpath
        '.' for class
        '#' for id
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

    def check_override(self):
        if self.override is None:
            log.debug("check_override() is NONE")
            return
        for key in self.override:
            log.debug("check_override() KEY: {}".format(key, ))
            if key in self.runtime:
                if type(self.runtime[key]) is tuple:
                    # Replace the 'value' portion
                    self.runtime[key] = (self.runtime[key][0],
                                         self.runtime[key][1],
                                         self.override[key])
                elif type(self.runtime[key]) is str:
                    self.runtime[key] = self.override[key]
        log.debug("check_override() new runtime: {}".format(self.runtime,))

    def check_for_placeholder(self, command, element):
        """
        Allows a placeholder inside an xpath, e.g. {
            'provider': '123456',
            'selectAssign': ("Click", '//*[@id="#provider;"]/div[1]', "")}
        :param command: string - command type, e.g. 'Click', 'Select', 'Chain'
        :param element: string - the element's location or xpath
        :return: string - element
        """
        # TODO: need a way to handle xpaths inside the Chain command, #90548734
        if command != 'Chain' and element.find('&') is not -1:
            # Look for placeholder key
            log.debug("------ ELEMENT: {}".format(element,))
            key = element[element.find('&') + 1: element.find(';')]
            log.debug("-- REPLACE KEY: {}".format(key, ))
            if key in self.runtime:
                element = element.replace(
                    '&{};'.format(key,), self.runtime[key])
                log.debug("-- NEW ELEMENT: {}".format(element, ))
        return element

    def teardown(self):
        # TODO: this should also be in the launch file vtf
        log.info("Teardown")
        self.wait(1)  # TODO: Remove later JNU!!!
        self.driver.quit()

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
