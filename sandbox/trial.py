import time
"""
Figure out how to use *args and **kwargs inside functions
"""


def results(expected, **value):
    locator = value.pop('locator', None)
    wait_time = value.pop('wait_time', 5)
    negative = value.pop('negative', False)
    message = value.pop('message', '')
    condition = value.pop('condition', 'presence_of_element_located')

    if value:  # all possible keys should be used at this point
        raise TypeError("Unsupported configuration options {}".format(value,))

    print("""
    EXPECTED: {0}
    LOCATOR: {1}
    WAIT TIME: {2}
    NEGATIVE: {3}
    MESSAGE: {4}
    CONDITION: {5}
    """.format(expected, locator, wait_time,
               negative, message, condition, ))


results("Expected Result", wait_time=8, locator='toast-container',
        condition='presence_of_element_located', message="Hello, world!",
        negative=True)

results("Expected Result", wait_time=15,
        condition='presence_of_element_located', message="Hello, world!")

results("Expected Result")

results("Expected Result", bogus="Where am I?")
