import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import InvalidElementStateException

import tool.utilities as utils
import book
from tool.vlog import VLog

__author__ = 'John Underwood'
"""
This class will setup the selenium driver and process all commands from
subclasses. This class drives the user interface (UI) testing framework.

Locator's Reference:
//xpath
.class
#id
<tag_name>
css=.class

Note:
This test uses the Chrome PDF Viewer, so it needs the following driver's option
added; see UI() class: add_experimental_option('excludeSwitches', ['test-type'])

An infobar warning banner will display, "You are using an unsupported
command-line flag: --ignore-certificate-errors. Stability and security will
suffer."

Alter the above to avoid the banner:
add_experimental_option(
    'excludeSwitches', ['test-type', 'ignore-certificate-errors'])
"""

log = VLog(name="vtf", log_name="UI")


class UI:

    # Menu - vertical nav bar starts from 1 down to n
    HOME = '1'
    WIKI = '2'
    MANAGE_ENTITIES = '3'
    MANAGE_JOBS = '4'
    REPORTS = '5'
    LICENSING = '6'
    SALES = '7'
    FILE = '8'
    WATCH = '9'
    ADMIN = '10'

    chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("window-size=1280,1024")
    chrome_options.add_argument("--disable-extensions")  # developer extensions
    # TODO: disable hardware acceleration setting - this doesn't work
    chrome_options.add_argument("--disable-gpu")
    # This option takes care of a known issue in the browser, where the
    # PDF viewer does not function as expected--it downloads the file.
    chrome_options.add_experimental_option(
        'excludeSwitches',
        ['test-type', 'ignore-certificate-errors'])
    username = utils.get_configurations('USER', 'username')
    driver = webdriver.Chrome(executable_path='C:/Common/chromedriver',
                              chrome_options=chrome_options)
    driver.get('http://{}:{}@indytest/'.format(username, book.password))  # TODO
    driver.implicitly_wait(5)  # seconds
    url = utils.url
    driver.get(url)  # TODO: combine the get() func above; hardcoded indytest/
    log.debug("TEST Uniform Resource Locator --------->>> {}".format(url,))
    assert "INDY" in driver.title

    max_size = int(utils.get_configurations("LOGGING", "max_string_size"))
    UNKNOWN = ("Unknown", "Unknown", "Unknown")  # (action, locator, value)

    runtime = {}
    override = {}

    def __init__(self, override=None):
        """
        Takes a dictionary where its key(s) overrides a given key(s) inside
        'runtime' and the value replaces runtime's field set to '__OVERRIDE__'
        :param override: dict
        :return: None
        """
        self.override = override
        log.debug("UI __init__() override: {}".format(override,))

    def update(self, runtime):
        log.trace("UI update()")
        self.runtime.update(runtime)
        self.check_override()

    def execute(self, items):
        """
        :param items: a tuple of keys; the keys reference 'override' dict
        :return: None
        Note: 'key' always expects a tuple of two elements with an optional
        third element for 'value'. (<action>, <locator>[, <value])
        Note: <locator> is an //xpath, .class, #id
        """
        for key in items:
            log.debug("Execute KEY:[{}]".format(key,))
            content = self.runtime.get(key, self.UNKNOWN)
            if content is not None:  # for this: override = {'showAll': None}
                self.exec_commands(content)

    def exec_commands(self, content):
        if len(content) == len(self.UNKNOWN):
            command, locator, value = content
        else:
            command, locator, value = content + ("", )

        # The 'locator' and 'value' both may have placeholders
        locator = self.check_for_placeholder(locator)
        if value.find('&') is not -1:
            log.debug("-- REPLACE a 'value'")
            value = self.check_for_placeholder(value)

        if command == "Click":
            self.click(locator)
        elif command == "Type":
            self.type(locator, value)
        elif command == "TypeInCkeditor":
            self.type_in_ckeditor(locator, value)
        elif command == "TypeAndTab":
            self.type_tab(locator, value)
        elif command == "Find":
            self.find(locator, value)
        elif command == "Select":
            self.select(locator, value)
        elif command == "Wait":
            self.wait_for_element(locator, value)
        elif command == "Chain":
            self.chain(locator)
        elif command == "Loop":  # temporarily for testing tables JNU!!!
            self.loop(locator)
        elif command == "Unknown":
            log.warning("""Execute - This command is unknown or
            runtime has not been processed""")
        else:
            log.exception("""Execute - No command is available -
            throw an error""")
        time.sleep(1)

    def click(self, locator):
        log.info("Click Command - PATH: {0}".format(locator))
        self.check_for_new_window()
        element = self.find_element(locator)
        element.click()

    def type(self, locator, value, char='$', **kwargs):
        """
        Do action of type (typewrite) in a value
        :param locator: element location in DOM
        :param value: string - value to type into the element
        :param char: string - special char that may not clear()
        :return: void
        """
        # Remove large string input for simpler logging.
        from selenium.webdriver.common.keys import Keys
        temp = value
        if len(value) > self.max_size and self.max_size is not 0:
            ellipsis = "..."
            temp = value[:self.max_size-len(ellipsis)].rstrip() + ellipsis
        log.info("Type Command - PATH: {0} - VALUE: \'{1}\'".
                 format(locator, temp))
        self.check_for_new_window()
        element = self.find_element(locator)
        try:
            element.clear()
            entry = self.get(locator, 'value')
            if char in entry:
                element.send_keys(Keys.CONTROL, 'a')
                element.send_keys(Keys.DELETE)
        except InvalidElementStateException:
            """invalid element state: Element must be user-editable in
            order to clear it."""
            log.warning("Element is not user-editable; unable to clear()")

        element.send_keys(value)

    def type_in_ckeditor(self, locator, value):
        """
        Do action of type (typewrite) in a value inside the ckeditor
        :param locator: element location in DOM
        :param value: string - value to type into the element
        :param char: string - special char that may not clear()
        :return: void
        """
        # Remove large string input for simpler logging.
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        temp = value
        if len(value) > self.max_size and self.max_size is not 0:
            ellipsis = "..."
            temp = value[:self.max_size-len(ellipsis)].rstrip() + ellipsis
        log.info("Type Command - PATH: {0} - VALUE: \'{1}\'".
                 format(locator, temp))
        self.check_for_new_window()
        element = self.find_element(locator)

        self.driver.switch_to.frame(element)  # switch to inside the iframe
        ck_editor_body = self.driver.find_element_by_tag_name('body')
        try:
            # Clear out any data inside the editor
            actions = ActionChains(self.driver)
            actions.click(ck_editor_body).key_down(Keys.CONTROL).send_keys(
                "a").key_up(Keys.CONTROL).perform()
            actions.send_keys(Keys.BACKSPACE).perform()
        except InvalidElementStateException:
            """invalid element state: Element must be user-editable in
            order to clear it."""
            log.warning("Element is not user-editable; unable to clear()")

        ck_editor_body.send_keys(value)
        self.driver.switch_to.default_content()  # get out of the iframe

    def type_tab(self, locator, value):
        """ MAY NOT NEED THIS FUNCTION JNU!!!
        Date or Time fields require a tabbing between sub-fields,
        i.e. 12 tab 21 tab 2015 OR 01 tab 15 tab pm
        month, day, year OR hour, minute, period (AM/PM)
        :param locator: element location in DOM
        :param value: requires formats "mmddyyyy" OR "hhmmpp"
        :return: void
        """
        log.info("Type Command - PATH: {0} - VALUE: \'{1}\'".
                 format(locator, value))
        # Get the three elements of either date or time
        # Date first = month, second = day, third = year
        # Time first = hour, second = minute, third = pm or am
        first, second, third = (value[:2], value[2:4], value[4:])
        self.check_for_new_window()
        element = self.find_element(locator)

        log.info("Month:{}".format(first, ))
        element.send_keys(first)  # month OR hour
        self.wait(5)
        log.info("Day:{}".format(second, ))
        element.send_keys("\t")
        element.send_keys(second)  # day OR minute
        self.wait(5)
        log.info("Year:{}".format(third, ))
        element.send_keys("\t")
        element.send_keys(third)  # year OR period

    def find(self, locator, value):
        """
        Special 'Type' case for the 'Find...' that requires no submit()
        :param locator: the 'Find...' DOM element
        :param value: the search string
        :return: None
        """
        log.info("Type Command for Find... - PATH: {0} - VALUE: \'{1}\'".
                 format(locator, value))
        self.check_for_new_window()
        element = self.find_element(locator)
        element.send_keys(value)

    def select(self, locator, value):
        """
        May want to add the other options such as by value and by index.
        See http://selenium-python.readthedocs.org/en/latest/api.html
        :param locator: holds the xpath, id, class, or tag
        :param value: visible text inside the list
        :return: None
        """
        log.info("Select Command - PATH: {0} - VALUE: \'{1}\'"
                 .format(locator, value))
        self.wait(1)  # compensate for on-screen shifting of the element
        self.check_for_new_window()
        element = self.find_element(locator)
        select = Select(element)
        if value == "":
            select.select_by_index(1)
        else:
            select.select_by_visible_text(value)

    def loop(self, elements):  # temporarily for testing tables JNU!!!
        # import xml.etree.ElementTree as ETree
        log.info("Elements: {}".format(elements))
        element = self.find_element(elements)
        log.info("Element: {}".format(element))

        # log.info("Loop Command - PATH: \'{0}\'".format(elements))
        # element = self.find_element(elements)
        # element.click()

    def chain(self, elements):
        """
        Builds an 'action chain' - add more actions as needed - see link
        'http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver/
            selenium.webdriver.common.action_chains.html'
        :param elements: Contains a list of tuples; tuple structure is
        (action, {param1:p1, param2:p1}, (etc.), etc.)
        :return: None
        Sample of the Chain:
          'correspond': ("Chain", [
              ('click', {
                  'on_element': '//*[@id="slide-out"]/li[8]/ul/li/a/i'}),
              ('click', {
                  'on_element': '//*[@id="slide-out"]/li[8]/ul/li/div/ul/li[1]/a'
          }),]),
        """
        actions = ActionChains(self.driver)
        # Build the actions chain
        for elem in elements:
            action, params = elem
            for k in params:  # only one element should be in dict at this point
                sub_locator = params.get(k, None)
                # The first argument 'check_chain' is a phony command;
                # a command is not necessary for chaining.
                replacer = self.check_for_placeholder(sub_locator)
                params[k] = replacer

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
                actions.drag_and_drop_by_offset(source, xoffset, yoffset)
            elif action == "move_to_element":
                to_element = self.find_element(params['to_element'])
                actions.move_to_element(to_element)
            log.info("Chained action: {0}".format(action, ))
        self.wait(1)
        actions.perform()

    def wait_for_element(self, elem_id, wait_time=1):
        """
        Waits for elements with the id attribute; id only
        :param elem_id: a string that holds the element's id
        :param wait_time: int - wait time in seconds
        :return: None
        Note: https://blog.mozilla.org/webqa/2012/07/12/how-to-webdriverwait/
        """
        wait_time = int(wait_time)  # will throw error if contains alpha chars
        _id = elem_id
        if elem_id[0:1] == "#":
            _id = elem_id[1:]  # remove the hash sign
        log.info("Wait Command - wait for id=\"{0}\"".format(elem_id))
        from selenium.webdriver.support import expected_conditions as ec
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        try:
            WebDriverWait(self.driver, wait_time).until(
                ec.presence_of_element_located((By.ID, _id)),
                "elem_id: {} - wait_time: {}".format(_id, wait_time,))
        finally:
            pass

    def find_element(self, locator):
        """
        '//' for xpath
        '.' for class
        '#' for id
        'css=' for css
        '<' for tag
        :param locator: a valid selector type, ie. xpath, class, id, css, or tag
        :return: the DOM's element
        Special case '<' looks for many tag elements; this helps get around
        the display of items that have dynamic id attribute,
        i.e. id="client_5568b9eecbc2e"
        """
        first_element = locator[0]
        if first_element == '/':  # xpath
            temp = self.driver.find_element_by_xpath(locator)
            return temp  # self.driver.find_element_by_xpath(elem)
        elif first_element == '.':  # ".<class>"
            _class = locator[1:]
            return self.driver.find_element_by_class_name(_class)
        elif first_element == '#':  # "#<id>"
            _id = locator[1:]
            return self.driver.find_element_by_id(_id)
        elif first_element == '<':  # "<<tag>>"-special case that looks for many
            # Returns the last element in the list; assumes the last element
            # is the desired element.
            _tag = locator[1:-1]
            return self.driver.find_elements_by_tag_name(_tag)[-1]
        elif locator[:3] == 'css':  # "css=<target>"
            _css = locator[4:]
            log.info("CSS element: {0}".format(_css))
            return self.driver.find_element_by_css_selector(_css)
        elif locator[:4] == 'name':  # "name=<target>"
            _name = locator[5:]
            log.info("'Name' element: {0}".format(_name))
            return self.driver.find_element_by_name(_name)
        else:
            # TODO: need to throw exception
            log.exception("no correct element found")

        return None

    def check_for_new_window(self):
        """
        Get the window handle of the new window and switch to that.
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
        self.wait(0.5)

    def check_override(self):
        """
        Override the key values inside runtime data
        :return: None
        """
        log.debug("check_override() override: {}".format(self.override,))
        if self.override is None:
            log.debug("check_override() is NONE")
            return
        for key in self.override:
            log.debug("check_override() KEY: [{}]".format(key, ))
            if key in self.runtime:
                if type(self.override[key]) is str:
                    # Replace the 'value' portion of the tuple
                    # Example: override = {'selectType': 'Doctorate Degree'}
                    log.debug("KEY is [{}] AND runtime[key]: {}".format(
                        key, self.runtime[key], ))
                    if len(self.runtime[key]) is tuple:  # value portion
                        self.runtime[key] = (self.runtime[key][0],  # action
                                             self.runtime[key][1],  # locator
                                             self.override[key])    # value
                    else:
                        self.runtime[key] = self.override[key]  # placeholder
                elif type(self.override[key]) is tuple:
                    self.runtime[key] = self.override[key]
                elif self.override[key] is None or self.override[key] == '':
                    # For this situation: override = {'showAll': None}
                    self.runtime[key] = None
                else:
                    log.exception("override has incorrect data structure")
            else:
                log.warning("The 'override' key is not found in 'runtime'")
        log.debug("check_override() new runtime: {}".format(self.runtime,))

    def check_for_placeholder(self, replacer):
        """
        Allows a placeholder inside an xpath, e.g. {
            'provider': '123456',
            'selectAssign': ("Click", '//*[@id="&provider;"]/div[1]', "")}
        The replacer param may hold something other than a string, i.e. Chain
        :param replacer: string - the element's location in the DOM
        :return: string - locator
        """
        if not isinstance(replacer, str):
            return replacer
        while utils.test_for_symbols(replacer):
            # Look for placeholder key
            log.debug("------ ELEMENT: {}".format(replacer,))
            key = replacer[replacer.find('&') + 1: replacer.find(';')]
            log.debug("-- REPLACE KEY: {}".format(key, ))
            if key in self.runtime:
                replacer = replacer.replace(
                    '&{};'.format(key,), self.runtime[key])
                log.debug("-- NEW ELEMENT: {}".format(replacer, ))
        return replacer

    def results(self, expected, elem_id=None, wait_time=5, negative=False):
        """
        Search the DOM for the expected string.
        :param expected: expected results search string
        :param elem_id: look in a DOM specific area using 'id' attribute
        :param wait_time: the total tolerance time
        :param negative: True - do NOT expect to see the expected
        :return: boolean
        """
        self.check_for_new_window()
        if elem_id:
            self.wait_for_element(elem_id.strip('#'), wait_time)
        html_source = self.driver.page_source.lower()
        res = True
        log.info("Expected is '{}'".format(expected))
        if expected.lower() in html_source and not negative:
            log.info("-- PASSED TEST CASE!!! ---")
        elif expected.lower() in html_source and negative:
            log.info("-- FAILED NEGATIVE TEST CASE!!! ---")
            res = False
        elif expected.lower() not in html_source and negative:
            log.info("-- PASSED NEGATIVE TEST CASE!!! ---")
        else:
            log.info("-- FAILED TEST CASE!!! --")
            res = False
        return res

    def get(self, locator, attribute_name):
        """
        Get an on-screen value
        :param locator: holds the xpath, id, class, or tag
        :param attribute_name: attribute name, i.e. innerHTML, value, name, etc.
        :return: string - value
        """
        locator = self.check_for_placeholder(locator)
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)

    def get_selected_option(self, locator):
        """
        Get an on-screen value
        :param locator: holds the xpath, id, class, or tag
        :return: string - value
        """
        element = self.find_element(locator)
        select = Select(element)
        return select.first_selected_option.get_attribute('value')

    def is_available(self, locator):
        """
        Is the action--click--available on the screen
        :param locator: holds the xpath, id, class, or selector
        :return: Boolean
        """
        from selenium.common.exceptions import WebDriverException
        element = self.find_element(locator)
        try:
            element.click()
        except WebDriverException as wde:
            log.info("is_available() exception - {}".format(wde, ))
            return False
        return True

    def dismiss_alert(self):
        """
        Dismisses (Cancel) the JavaScript alert dialog box.
        :return: String - the alert's text
        """
        alert_message = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.dismiss()
        return alert_message

    def accept_alert(self):
        """
        Accepts (OK) the JavaScript alert dialog box.
        :return: String - the alert's text
        """
        alert_message = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert_message

    def teardown(self):
        log.info("Teardown")
        self.wait(1)
        self.driver.quit()

    @staticmethod
    def compare(expected, actual):
        if actual == expected:
            log.debug("PASSED: actual '{}' is same as expected '{}'".
                      format(actual, expected, ))
            return True
        else:
            log.debug("FAILED: actual '{}' is different from expected '{}'".
                      format(actual, expected, ))
            return False

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
