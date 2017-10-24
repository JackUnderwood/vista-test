import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import tool.utilities as utils
# import book
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

    url = utils.url
    # Get configurations
    username = utils.get_configurations('USER', 'username')
    driver_location = utils.get_configurations('CHROME', 'driver')

    chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("window-size=1280,1024")  # 1280x1024 resolution
    chrome_options.add_argument("--disable-extensions")  # developer extensions
    # TODO: disable hardware acceleration setting - this doesn't work
    chrome_options.add_argument("--disable-gpu")
    # This option takes care of a known issue in the browser, where the
    # PDF viewer does not function as expected--it downloads the file.
    chrome_options.add_experimental_option(
        'excludeSwitches',
        ['test-type', 'ignore-certificate-errors'])
    driver = webdriver.Chrome(executable_path=driver_location,
                              chrome_options=chrome_options)
    # driver.get('http://{}:{}@indytest/'.format(username, book.password)) # TODO
    driver.implicitly_wait(20)  # in seconds
    driver.get(url)
    log.debug("TEST Uniform Resource Locator --------->>> {}".format(url, ))
    assert "INDY" in driver.title

    max_size = int(utils.get_configurations("LOGGING", "max_string_size"))
    log_path = utils.get_configurations("DEFAULT", "log_path")
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

    def exec_commands(self, content):  # JNU!!! not a 'command', but an 'action'
        if len(content) == len(self.UNKNOWN):
            command, locator, value = content
        else:
            command, locator, value = content + ("", )

        # The 'locator' and 'value' both may have placeholders
        locator = self.check_for_placeholder(locator)
        if isinstance(value, str) and value.find('&') is not -1:
            log.debug("-- REPLACE a 'value'")
            value = self.check_for_placeholder(value)

        if command == "Click":
            self.click(locator)
        elif command == "Type":
            self.type(locator, value)
        elif command == "TypeInCkeditor":
            self.type_in_ckeditor(locator, value)
        elif command == "TypeAndTab":
            self.type_and_tab(locator, value)
        elif command == "Find":
            self.find(locator, value)
        elif command == "Select":
            self.select(locator, value)
        elif command == "Upload":
            self.upload(locator, value)
        elif command == "Hover":
            self.hover(locator)
        elif command == "Wait":
            self.wait_for_element(locator, **value)
        elif command == "Chain":
            self.chain(locator)
        elif command == "Loop":  # temporarily for testing tables JNU!!!
            self.loop(locator)
        elif command == "Unknown":
            log.warning("""Execute - This command is unknown or
            runtime has not been processed or 'order' value is
            mismatch to key""")
        else:
            log.exception("""Execute - No command is available -
            throw an error""")
        time.sleep(1)

    def click(self, locator):
        log.info("CLICK command using LOCATOR: {0}".format(locator))
        self.check_for_new_window()
        element = self.find_element(locator)
        element.click()

    def type(self, locator, value, char='$'):
        """
        Do action of typing (typewrite) in a value
        :param locator: element location in DOM
        :param value: string - value to type into the element
        :param char: string - special char that may not clear()
        :return: void
        """
        from selenium.webdriver.common.keys import Keys
        log.info("TYPE command using LOCATOR: {} :: VALUE: \'{}\'".
                 format(locator, self.truncate(value, max_size=self.max_size)))
        self.check_for_new_window()
        element = self.find_element(locator)
        try:
            element.clear()
            entry = self.spy(locator, 'value')
            if char in entry:
                element.send_keys(Keys.CONTROL, 'a')
                element.send_keys(Keys.DELETE)
        except InvalidElementStateException:
            """invalid element state: Element must be user-editable in
            order to clear it."""
            log.warning("Element is not user-editable; unable to clear()")
        self.wait()
        element.send_keys(value)

    def type_in_ckeditor(self, locator, value):
        """
        Do action of typing in a value inside the ckeditor
        :param locator: element location in DOM
        :param value: string - value to type into the element
        :return: void
        """
        # Remove large string input for simpler logging.
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        log.info("TYPE_IN_CKEDITOR command using LOCATOR: {0} - VALUE: \'{1}\'".
                 format(locator, self.truncate(value, max_size=self.max_size)))
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

    def type_and_tab(self, locator, value):
        """
        :param locator: element location in DOM
        :param value: string - value to type into the element
        :return: void
        """
        log.info("TypeAndTab Command - PATH: {0} - VALUE: \'{1}\'".
                 format(locator, value))
        self.type(locator, value)
        element = self.find_element(locator)
        element.send_keys("\t")

    def type_date_tab(self, locator, value):
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

        log.info("Month:{}".format(first,))
        element.send_keys(first)  # month OR hour
        self.wait(5)
        log.info("Day:{}".format(second,))
        element.send_keys("\t")
        element.send_keys(second)  # day OR minute
        self.wait(5)
        log.info("Year:{}".format(third,))
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
        self.wait()  # compensate for on-screen shifting of the element
        self.check_for_new_window()
        element = self.find_element(locator)
        select = Select(element)
        if value == "":
            select.select_by_index(1)
        else:
            select.select_by_visible_text(value)
        self.wait()

    def upload(self, locator, value):
        """
        See http://www.seleniumstutorial.com/
        uploading-a-file-in-selenium-with-python/
        :param locator: string - holds the xpath, id, or class
        :param value: string - file's path on local drive, e.g. 'c:/tmp/file.txt'
        :return: None
        """
        log.info("Upload Command - LOCATOR: {0} - VALUE: \'{1}\'"
                 .format(locator, value))
        element = self.find_element(locator)
        element.send_keys(value)

    def hover(self, locator):
        """
        Move mouse over element and wait there for next action.
        Note: Uses the ActionChains
        :param locator: holds the xpath, id, class, or tag
        :return: None
        """
        log.info("Hover Command - PATH: {0}".format(locator,))
        self.wait(2)  # critical wait --
        actions = ActionChains(self.driver)
        element = self.find_element(locator)
        actions.move_to_element(element).perform()
        self.wait()

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
        Used to access the navigation menu
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
            log.info("Chained action: {0}".format(action,))
        self.wait(1)
        actions.perform()

    def wait_for_element(self, locator, **value):
        """
        Waits for the element to appear.
        e.g. ('Wait', '#scratch-pad', {'condition': 'element_to_be_clickable'})
        :param locator: a string that holds the element's id, xpath, class,
        or css selector
        :param value: dict - may contain keys 'wait_time' and 'condition'; a list
        of available conditions is found in self.get_expected_condition()
        :return: None
        Note: https://blog.mozilla.org/webqa/2012/07/12/how-to-webdriverwait/
        Note: http://selenium-python.readthedocs.io/waits.html#explicit-waits
        """
        wait_time = value.pop('wait_time', 5)
        condition = value.pop('condition', 'presence_of_element_located')
        if value:  # all possible keys should be used at this point
            raise TypeError("Unsupported configuration options {}".
                            format(value,))

        _condition = self.get_expected_condition(condition)
        if _condition is None:
            raise ValueError("Unsupported wait condition: {}".format(condition,))

        wait_time = int(wait_time)  # will throw error if contains alpha chars
        _locator = locator  # default to element's id, e.g. 'toast-container'
        _by = By.ID
        if locator.startswith('#'):
            _locator = locator[1:]  # remove hash sign, e.g. '#toast-container'
            _by = By.ID
        elif locator.startswith('/'):
            _by = By.XPATH
        elif locator.startswith('.'):
            _locator = locator[1:]  # remove the full stop
            _by = By.CLASS_NAME
        elif locator.startswith('css='):
            _locator = locator[4:]
            _by = By.CSS_SELECTOR
        elif locator.startswith('<'):
            _locator = locator[1:-1]  # remove gt and lt signs
            _by = By.TAG_NAME
        else:
            pass

        log.info("Wait action: wait_for_element --> \"{0}\"".format(locator,))
        try:
            wait = WebDriverWait(self.driver, wait_time)
            _message = "Waiting for element: {}".format(_locator,)
            wait.until(_condition((_by, _locator)), message=_message)
        except TypeError as te:
            log.error(
                "wait_for_element: Expected condition failed to execute: {}"
                .format(te))
        finally:
            pass

    def wait_for_title(self, title, wait_time=5):
        from selenium.common.exceptions import TimeoutException
        wait = WebDriverWait(self.driver, wait_time)
        try:
            wait.until(lambda x: title in self.driver.title)
        except TimeoutException as te:
            log.error(
                'wait_for_title: Timeout exception: {}'.format(te,))
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
        i.e. id="client_5568b9"
        """
        element = None
        if locator.startswith('/'):  # xpath
            try:
                element = self.driver.find_element_by_xpath(locator)
            except NoSuchElementException as nsee:
                log.error('find_element: xpath exception: {}'.format(nsee,))
            return element  # self.driver.find_element_by_xpath(elem)

        elif locator.startswith('.'):  # ".<class>"
            _class = locator[1:]
            try:
                element = self.driver.find_element_by_class_name(_class)
            except NoSuchElementException as nsee:
                log.error('find_element: xpath exception: {}'.format(nsee,))
            return element

        elif locator.startswith('#'):  # "#<id>"
            _id = locator[1:]
            try:
                element = self.driver.find_element_by_id(_id)
            except NoSuchElementException as nsee:
                log.error('find_element: xpath exception: {}'.format(nsee,))
            return element

        elif locator.startswith('<'):  # "<<tag>>"--a case that looks for many
            # Returns the last element in the list; assumes the last element
            # is the desired element.
            _tag = locator[1:-1]
            try:
                element = self.driver.find_elements_by_tag_name(_tag)[-1]
            except NoSuchElementException as nsee:
                log.error('find_element: xpath exception: {}'.format(nsee,))
            return element

        elif locator.startswith('css'):  # "css=<target>"
            _css = locator[4:]
            try:
                element = self.driver.find_element_by_css_selector(_css)
                log.info("CSS element: {0}".format(_css))
            except NoSuchElementException as nsee:
                log.error('find_element: xpath exception: {}'.format(nsee,))
            return element

        elif locator.startswith('name'):  # "name=<target>"
            _name = locator[5:]
            try:
                log.info("'Name' element: {0}".format(_name))
                element = self.driver.find_element_by_name(_name)
            except NoSuchElementException as nsee:
                log.error('find_element: xpath exception: {}'.format(nsee,))
            return element

        else:
            # TODO: need to throw exception
            log.exception("no correct element found")
        return element

    def find_elements(self, locator):
        """
        '//' for xpath
        '.' for class
        '#' for id
        'css=' for css
        '<' for tag
        :param locator: a valid selector type, ie. xpath, class, id, css, or tag
        :return: a list of the DOM's elements
        Special case '<' looks for many tag elements; this helps get around
        the display of items that have dynamic id attribute,
        i.e. id="client_5568b9"
        """
        elements = []
        if locator.startswith('/'):  # xpath
            try:
                elements = self.driver.find_elements_by_xpath(locator)
            except NoSuchElementException as nsee:
                log.error('find_elements: xpath exception: {}'.format(nsee,))
            return elements

        elif locator.startswith('.'):  # ".<class>"
            _class = locator[1:]
            try:
                elements = self.driver.find_elements_by_class_name(_class)
            except NoSuchElementException as nsee:
                log.error('find_elements: xpath exception: {}'.format(nsee,))
            return elements

        elif locator.startswith('#'):  # "#<id>"
            _id = locator[1:]
            try:
                elements = self.driver.find_elements_by_id(_id)
            except NoSuchElementException as nsee:
                log.error('find_elements: xpath exception: {}'.format(nsee,))
            return elements

        elif locator.startswith('<'):  # "<<tag>>"--a case that looks for many
            # Returns the last element in the list; assumes the last element
            # is the desired element.
            _tag = locator[1:-1]
            try:
                elements = self.driver.find_elements_by_tag_name(_tag)[-1]
            except NoSuchElementException as nsee:
                log.error('find_elements: xpath exception: {}'.format(nsee,))
            return elements

        elif locator.startswith('css'):  # "css=<target>"
            _css = locator[4:]
            try:
                elements = self.driver.find_elements_by_css_selector(_css)
                log.info("CSS element: {0}".format(_css))
            except NoSuchElementException as nsee:
                log.error('find_elements: xpath exception: {}'.format(nsee,))
            return elements

        elif locator.startswith('name'):  # "name=<target>"
            _name = locator[5:]
            try:
                elements = self.driver.find_elements_by_name(_name)
                log.info("'Name' element: {0}".format(_name))
            except NoSuchElementException as nsee:
                log.error('find_elements: xpath exception: {}'.format(nsee,))
            return elements

        else:
            # TODO: need to throw exception
            log.exception("no correct elements found")

        return elements

    def scroll_to_bottom_of_page(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.wait()

    def scroll_to_top_of_page(self):
        self.driver.execute_script(
            "window.scrollTo(0, 0);")
        self.wait()

    def find_elements_by_class_name(self, class_name):
        """
        Wrapper - Finds elements by class name.
        :param class_name: The class name of the elements to find.
        :return: list of elements
        """
        return self.driver.find_elements_by_class_name(class_name)

    def check_for_new_window(self):
        """
        Get the window handle of the new window and switch to that.
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
        self.wait()

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
            log.debug("check_override() KEY: [{}]".format(key,))
            if isinstance(self.override[key], int):
                self.override[key] = str(self.override[key])
            if key in self.runtime:
                # if type(self.override[key]) is str:
                if isinstance(self.override[key], str):
                    # Replace the 'value' portion of the tuple
                    # Example: override = {'selectType': 'Doctorate Degree'}
                    log.debug("KEY is [{}] AND runtime[key]: {}".format(
                        key, self.runtime[key],))
                    if len(self.runtime[key]) is tuple:  # value portion
                        self.runtime[key] = (self.runtime[key][0],  # action
                                             self.runtime[key][1],  # locator
                                             self.override[key])    # value
                    else:
                        self.runtime[key] = self.override[key]  # placeholder
                # elif type(self.override[key]) is tuple:
                elif isinstance(self.override[key], tuple):
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
            log.debug("-- REPLACE KEY: {}".format(key,))
            if key in self.runtime:
                replacer = replacer.replace(
                    '&{};'.format(key,), self.runtime[key])
                log.debug("-- NEW ELEMENT: {}".format(
                    self.truncate(replacer), ))
            else:
                message = ("Trying to replace the placeholder \"{}\""
                           "with the non-existing KEY [{}]")
                raise KeyError(message.format(replacer, key))
        return replacer

    def results(self, expected, **value):
        """
        Search the DOM for the expected string.
        :param expected: expected results search string
        :param value: dict - contains several configurations--see value.pop code
        :return: boolean
        """
        locator = value.pop('locator', None)
        negative = value.pop('negative', False)
        message = value.pop('message', '')

        self.check_for_new_window()
        if locator:
            self.wait_for_element(locator, **value)
        html_source = self.get_source()
        res = True
        addendum = (
            " ::Addendum:: {}".format(message, ) if (message != '') else message)
        log.info("Expected is '{}'{}".format(expected, addendum))
        if expected.lower() in html_source and not negative:
            log.info("-- PASSED TEST CASE!!! ---")
        elif expected.lower() in html_source and negative:
            log.info("-- FAILED NEGATIVE TEST CASE ###### ---")
            res = False
        elif expected.lower() not in html_source and negative:
            log.info("-- PASSED NEGATIVE TEST CASE!!! ---")
        else:
            log.info("-- FAILED TEST CASE ###### --")
            res = False
        return res

    def get(self, url_path):
        """
        Loads a web page in the current browser session.
        :param url_path: string - partial path, e.g. 'jobs/search'
        :return: None
        """
        self.driver.get(self.url + url_path)

    def get_source(self):
        """
        Returns the current page's HTML source in lower case.
        :return: string - HTML body
        """
        return self.driver.page_source.lower()

    def get_table_size(self, locator, sep='\n'):
        """
        Returns the number of <tr> tags in the table.
        :param locator: string - a valid selector type, ie. xpath, id, etc.
        :param sep: string - separator/delimiter for the element's text
        :return: integer - table size; 'count' of table rows
        Note: The 'res[0]' may be the <thead> element, so may need to compensate
        for that.
        """
        element = self.find_element(locator)
        text = element.text
        res = text.split(sep)
        return len(res)

    def spy(self, locator, attribute_name):
        """
        Get an on-screen value
        :param locator: holds the xpath, id, class, or tag
        :param attribute_name: attribute name, i.e. innerHTML, value, name, etc.
        :return: string - value
        """
        attribute = None
        locator = self.check_for_placeholder(locator)
        try:
            element = self.find_element(locator)
            attribute = element.get_attribute(attribute_name)
        except NoSuchElementException as nsee:
            log.warning(msg='spy element is not available::{}'.format(nsee,))
        except AttributeError as ae:
            log.warning(msg='spy attribute is not available::{}'.format(ae,))

        return attribute

    def get_selected_option(self, locator, attribute_name='value'):
        """
        Get an on-screen option value from SELECT (drop down) object
        :param locator: holds the xpath, id, class, or tag of SELECT object
        :param attribute_name: string - value, text, name, etc.
        :return: string - value
        """
        element = self.find_element(locator)
        select = Select(element)
        return select.first_selected_option.get_attribute(attribute_name)

    def get_css_property(self, locator, css_selector):
        """
        Get the value of a CSS property.
        :param locator: holds the xpath, id, or class
        :param css_selector: 
        :return: string - property's value
        """
        element = self.find_element(locator)
        value = element.value_of_css_property(css_selector)
        return value

    def is_available(self, locator):
        """
        Is the element available on the screen
        :param locator: holds the xpath, id, class, or selector
        :return: Boolean
        """
        try:
            element = self.find_element(locator)
            element.click()
        except NoSuchElementException as nsee:
            log.info("is_available() exception - {}".format(nsee,))
            return False
        return True

    def is_selected(self, locator):
        """
        Checks to see if checkbox is checked.
        :param locator: string - the xpath, id, class, or selector
        :return: Boolean
        """
        element = self.find_element(locator)
        res = element.is_selected()
        return res

    def dismiss_alert(self):
        """
        Dismisses (Cancel) the JavaScript alert dialog box.
        :return: String or None - the alert's text OR alert not there
        """
        alert_message = None
        try:
            alert_message = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.dismiss()
            log.info(msg='Dismissed alert')
        except TimeoutException:
            log.info(msg='No alert is available')
        return alert_message

    def accept_alert(self):
        """
        Accepts (OK) the JavaScript alert dialog box.
        :return: String or None - the alert's text OR alert not there
        """
        alert_message = None
        try:
            alert_message = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
            log.info(msg='Accepted alert')
        except NoAlertPresentException:
            log.info(msg='No alert present')
        except TimeoutException:
            log.info(msg='No alert is available')
        return alert_message

    def go_to_url(self, url):
        """
        Redirect to a different location
        Deprecated - use the get() function above.
        :param url: string - in the form of a url
        """
        self.driver.get(url)

    def snapshot(self, filename):
        """
        Save a snapshot of the browser's current state.
        :param filename: string - file path, e.g. "snap1.png"
        :return: None
        """
        full_log_path = self.log_path + filename
        self.driver.save_screenshot(full_log_path)

    def teardown(self):
        """
        :return: void
        """
        log.info(time.strftime("%Y-%m-%d %H:%M"))
        log.info("Teardown")
        self.wait(1)
        self.driver.quit()

    @staticmethod
    def truncate(value, max_size=25, suffix='...'):
        """
        Remove large string input for simpler logging.
        Note: doesn't include the first word that may be longer than the max_size
        Note: rounds up a word, so if a max_size is in the middle of a word,
        the word is included in the returned string.
        See http://stackoverflow.com/questions/250357
        /truncate-a-string-without-ending-in-the-middle-of-a-word
        :param value: string - the value that may need to be truncated
        :param max_size: int - the maximum tolerance of the 'value'
        :param suffix: string - the last characters to indicate continuation
        :return: string
        """
        if len(value) <= max_size:
            return value
        else:
            num_of_words = len(value[:max_size].split())
            suffix = suffix if num_of_words > 1 else ""
            return ' '.join(value.split(' ')[0:num_of_words]) + suffix

    @staticmethod
    def get_expected_condition(condition):
        """
        This is used by wait_for_element() function above.
        :param condition: string - the condition's name
        :return: ec object -  expected condition object
        """
        if condition == "alert_is_present":
            return ec.alert_is_present
        elif condition == "element_located_selection_state_to_be":
            return ec.element_located_selection_state_to_be
        elif condition == "element_located_to_be_selected":
            return ec.element_located_to_be_selected
        elif condition == "element_selection_state_to_be":
            return ec.element_selection_state_to_be
        elif condition == "element_to_be_clickable":
            return ec.element_to_be_clickable
        elif condition == "element_to_be_selected":
            return ec.element_to_be_selected
        elif condition == "frame_to_be_available_and_switch_to_it":
            return ec.frame_to_be_available_and_switch_to_it
        elif condition == "invisibility_of_element_located":
            return ec.invisibility_of_element_located
        elif condition == "presence_of_all_elements_located":
            return ec.presence_of_all_elements_located
        elif condition == "presence_of_element_located":
            return ec.presence_of_element_located
        elif condition == "staleness_of":
            return ec.staleness_of
        elif condition == "text_to_be_present_in_element":
            return ec.text_to_be_present_in_element
        elif condition == "text_to_be_present_in_element_value":
            return ec.text_to_be_present_in_element_value
        elif condition == "title_contains":
            return ec.title_contains
        elif condition == "title_is":
            return ec.title_is
        elif condition == "visibility_of":
            return ec.visibility_of
        elif condition == "visibility_of_element_located":
            return ec.visibility_of_element_located
        return None

    @staticmethod
    def compare(expected, actual, message=''):
        """
        :param expected: variable type
        :param actual: variable type
        :param message: string
        :return: Boolean
        """
        addendum = (
            " ::Addendum:: {}".format(message, ) if (message != '') else message)
        if actual == expected:
            log.debug("PASSED: actual '{}' is same as expected '{}'{}".
                      format(actual, expected, addendum))
            return True
        elif not isinstance(expected, bool) and expected in actual:
            log.debug("PASSED: actual '{}' is part of expected '{}'{}".
                      format(actual, expected, addendum))
            return True
        else:
            log.debug("FAILED: actual '{}' is different from expected '{}'{}".
                      format(actual, expected, addendum))
            return False

    @staticmethod
    def wait(seconds=1):
        """
        :param seconds: integer
        :return: void
        """
        time.sleep(seconds)
